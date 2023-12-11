# Shard Cleanup in SQL Server

This TSG provides the steps to cleanup shard to recapture the disk space. This is a lot of manual effort and the cleanup will be a time consuming process.

### Steps to cleanup Shard
1. Identify the Shard where the cleanup or data has to be deleted and the External Source Id. Here is the query to find the External Source Id.

    `Select * from ExternalSource where ExternalSourceName='GenevaActions';`
    
      Here are the SQL Details. We can connect to the SQL Server from the dev machine using the `SQL Server Management Studio`

      | # | Environment  | Write SQL Connection | Database| Username| Password |
      |----|---------|-------------------------------|--|--|--|
      | 1  | PPE  |cvdc20gaea.database.windows.net|MSChange|MSChangeSQLUser|[FCMPPESQLPassword](https://ms.portal.azure.com/#@microsoft.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Secret/https://fcmintkv.vault.azure.net/secrets/FCMPPESQLPassword)|
      | 2  | PROD |x2altnc1cm.database.windows.net|MSChange|MSChangeSQLUser|[FCMPRODSQLPassword](https://ms.portal.azure.com/#@microsoft.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Secret/https://fcmintkv.vault.azure.net/secrets/FCMSQLProdPassword)|

2. Get the JIT access to view the Shard remaining space on the portal and access the below links from SAW Machine. Navigate to the Shard, available space will be displayed in the overview. 
      1. For PPE, get JIT for Subscription: 6ac089d6-2695-4daf-95df-ea06d302b618. 
            1. Link to the [PPE Write SQL Server](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/6ac089d6-2695-4daf-95df-ea06d302b618/resourceGroups/Default-SQL-WestUS/providers/Microsoft.Sql/servers/cvdc20gaea/overview)
      2. For PROD, get JIT for Subscription: fbc17084-a3a3-42bf-a9dc-8bc7f996a679. 
            1. Link to the [PROD Write SQL Server](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/fbc17084-a3a3-42bf-a9dc-8bc7f996a679/resourceGroups/Default-SQL-WestUS/providers/Microsoft.Sql/servers/x2altnc1cm/overview)
    
2. There are 3 main tables where we need to delete the data and are to be deleted in this order.
    `ChangeRecordXServiceTree, ChangeRecordXLocation, ChangeRecord are the three tables to be cleaned up.`
3. For all these 3 tables, there will be millions of records to be deleted. Delete them on a weekly basis. Don't delete the entire data at once as it may lock the entire table and cause ingestion issues. For example if you wanted to delete the entire data for a specific External Source, delete statements will be run 52 times, one time for each week.
4. Delete the records from ChangeRecordXServiceTree table.
    `delete  from ChangeRecordXServiceTree where FKExternalSourceId=? and Modified<'?'`
5. Verify the records are deleted by running the below query. Count returned should be 0. Use the last date used to run the above query. For example, if you are deleting from 01-01-2012 to 12-31-2021. Use the 12-31-2021 date in the below query.
    `select count(*)  from ChangeRecordXServiceTree where FKExternalSourceId=? and Modified<'?'`
6. Once all the target data/records is deleted from the ChangeRecordXServiceTree table, please run the update statistics on the table. This step took me an hour or so when I ran it last time.
    `UPDATE STATISTICS  ChangeRecordXServiceTree WITH FULLSCAN`
7. Delete the records from ChangeRecordXLocation table.
    `delete from ChangeRecordXLocation where FKExternalSourceId=? and Modified<'?';`
8. Verify the records are deleted by running the below query. Count returned should be 0. Use the last date used to run the above query. For example, if you are deleting from 01-01-2012 to 12-31-2021. Use the 12-31-2021 date in the below query.
    `select count(*)  from ChangeRecordXLocation where FKExternalSourceId=? and Modified<'?'`
9. Once all the target data/records is deleted from the ChangeRecordXLocation table, please run the update statistics on the table. This step took me 2 hours of time when I ran it last time.
    `UPDATE STATISTICS  ChangeRecordXLocation WITH FULLSCAN`
10. Delete the data from ChangeRecord Table. Replace the question mark with ExteranlSourceId and the date. 
        `delete  from ChangeRecord where FKExternalSourceId=? and Modified<'?' and ChangeRecordId not in ( Select FKChangeRecordId from IncidentXChangeRecord where FKExternalSourceId = ?);`
11. Verify the records are deleted by running the below query. Count may not return 0 as we are excluding the records in the above step. It may return return in 1000s depending on how many entries we have in the IncidentXChangeRecord table for that Source. Use the last date used to run the above query. For example, if you are deleting from 01-01-2012 to 12-31-2021. Use the 12-31-2021 date in the below query.
    `select count(*)  from ChangeRecord where FKExternalSourceId=? and Modified<'?'`
12. Once all the target data/records is deleted from the ChangeRecord table, please run the update statistics on the table. This took me around 7 hours of time when I ran it last time.
    `UPDATE STATISTICS  ChangeRecord WITH FULLSCAN`