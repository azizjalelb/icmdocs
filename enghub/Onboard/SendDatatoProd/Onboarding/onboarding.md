# Onboarding New Change System to FCM to send their changes to FCM via SDK

## Onboard to FCM PPE:

In order for customers to send changes to FCM PPE, they require access to `fcmonboardtest` keyvault  (https://fcmonboardtest.vault.azure.net/). This keyvault is in our corp subscription, `FCMProductionTransfer` (3a94e972-dca2-4a80-a437-5e856903d74a). In order to provide access to this keyvault, the app id of our customer needs to be added to 
`FcmOnBoardTest` UserGroup. In order to that:
    1. Go to Azure Portal
    2. Go to Azure Active Directory
    3. Select Groups from the left panel
    4. Search and select `FcmOnBoardTest`
    5. Go to `Members` from the left panel and add the app Id of the customer to direct members.
If for any reason, this doesn’t work, you can give the app Id of the customer a `Get,List` access to the fcmonboardtest keyvault directly.
At this point, the user should be able to send their changes to FCM PPE and see their changes under EventRouterSample change source system if they followed the guidelines for sending changes to FCM PPE.

## Onboard to FCM PROD:
#### Step 1: Add AppId to `FCMProdApps` user group.
In order for customers to send changes to FCM Prod, they require access to `fcmerhub` keyvault  (https://fcmerhub.vault.azure.net/). This keyvault is in our corp subscription, `FCMProductionTransfer` (3a94e972-dca2-4a80-a437-5e856903d74a). In order to provide access to this keyvault, the app id of our customer needs to be added to 
`FCMProdApps` UserGroup. In order to that:

1.	Go to Azure Portal
2.	Go to Azure Active Directory
3.	Select Groups from the left panel
4.	Search and select `FCMProdApps`
5.	Go to `Members` from the left panel and add the app Id of the customer to direct members. If for any reason, this doesn’t work, you can give the app Id of the customer a Get,List access to the fcmerhub keyvault directly.

`If the Customer App ID is from AME tenant,S grant the access to the keyvault: fcmamehub in the Production Subscription.`

#### Step 2: Add SourceName to database 
1. Update the ExternalSource table in all four primary write(shard) dbs. Insert the externalsource record in all the four primary write (shard) dbs.

    1. Connect Our primary sql server is `x2altnc1cm.database.windows.net` using Microsoft SQL Server Management Studio.
    2. Externalsourceid is a running number, get the next number by running the following query:
    
    `SELECT * FROM [dbo].[ExternalSource]`

    3. We have 4 shards: `mschangeshard_0, mschangeshard_1, mschangeshard_2, mschangeshard_3`. After getting next number,  run the following query in all of those shards to insert the new source system in to the db. Don’t forget to change to value placeholders with the real ones
    
    `INSERT INTO [dbo].[ExternalSource] VALUES (ExternalSourceId,'ExternalSourceName', 'Description','', '');`

2. Run powershell script for Writes  
    Step 1: Get JIT Access to our production subscriptions. Go to powershell, run the following command and login with your AME account.
    `Login-AzureRmAccount `
    
    Step 2:  Execute powershell script `AddnewExternalSourceToShardToWrite.ps1` (https://msazure.visualstudio.com/DefaultCollection/One/_git/EngSys-ChangeManagement-FCM?path=/src/FCM/Msdial.Change.Deployment/Shard/Powershell) in   
    Powershell - Repos (visualstudio.com)

    Follow the instructions in the comments of  the powershell script. You need to update the ExternalSource, which ShardDb the record will go to and the password. You can find the password in `Secret-FCMSQLPassword - Microsoft Azure`  (https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Secret/https://fcmproduction-kv.vault.azure.net/secrets/Secret-FCMSQLPassword) 

3. Validate the write DBs    
    Run this on the Shard Write DB  
    `SELECT [MappingId]  
        ,[Readable]  
        ,[ShardId]  
        ,[ShardMapId]  
        ,[OperationId]  
        ,[MinValue]  
        ,[MaxValue]  
        ,[Status]  
        ,[LockOwnerId]  
    FROM [__ShardManagement].[ShardMappingsGlobal]  `
    
    It should show the new externalSource in MinValue field in Hex format  
    
    Run this in the specific Shard db where   
    `SELECT [MappingId]  
        ,[ShardId]  
        ,[ShardMapId]  
        ,[MinValue]  
        ,[MaxValue]  
        ,[Status]  
        ,[LockOwnerId]  
        ,[LastOperationId]  
    FROM [__ShardManagement].[ShardMappingsLocal]  
    ORDER BY MinValue  `


#### Step 3: Stop and Start the Connectors and Web API

Resources to be Stopped and Started:
    1. `prodcustomeventconnectorwestus`
    2. `prodstandarddeploymenteventconnectorwestus`
    3. `prodwebapiwriteeastus`
    4. `prodwebapiwritewestus`

Stopping of resources should be done in the order listed above and the starting of them should be done in reverse order i.e. webapis to be started first and then the connectors

In order to stop and start,

    1.	Stop the resource from the overview tab
    2.	Wait until all of the instances are in the `Destroyed` state
    3.	Start the resource from the overview tab in the reverse order
    4.	Make sure that all of the instances are in ‘Started’ state