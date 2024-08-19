# Whitelist a subscription

## Overview

A valid service or subscription, not registered in Service Tree, will be blocked to deploy because Change Guard cannot find information about it to complete the workflow. It is from Service Tree the information is retrieved on who the approvers are for the service or
subscription; without that information it's impossible to create exception requests or to authorize them.

Whitelisting a subscription, pre-authorize all deployments to such subscription, to all regions.

Get approval from FCM manager, or any other manager above FCM manager before whitelisting a subscription

## Execution instructions

1. Connect to **chggrd-api-sql-svr-prod.database.windows.net** server using SSMS.
    - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
    - Use Entra Authentication along with your `@ame.gbl` account to connect to the server.
      - ![ssms](media/SSMS_prod_server.png)
    - To get write access to the SQL Database, see: [Granting `write` access to SQL Database through JIT](JITAccessToSQLDatabase.md)

2. Once logged into SSMS, connect to **chggrd-api-sql-db-prod** database and open the query window.
3. Run the following query:
   ``` 
      DECLARE @RC int 
      DECLARE @WhitelistedId nvarchar(50) = «WhitelistedId»
      DECLARE @WhitelistedLevel nvarchar(50) = «WhitelistedLevel»
      DECLARE @EventId nvarchar(1000) = «EventId»

      EXECUTE @RC = [dbo].[WhitelistIds]
          @WhitelistedId
         ,@WhitelistedLevel
         ,@EventId;

      SELECT @RC
   ``` 
   > [!NOTE]
   > - Replace **«WhitelistedId»** with the service or subscription id value.
   > - Replace **«WhitelistedLevel»** with the level of the id: Service | Subscription.
   > - Replace **«EventId»** with the id of the event during which this whitelisted Id is valid.
   > - If the event doesn't exist an exception is thrown and nothing is added. 