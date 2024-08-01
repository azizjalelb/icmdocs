# Whitelist a subscription

## Overview

A valid service or subscription, not registered in Service Tree, will be blocked to deploy because Change Guard cannot find information about it to complete the workflow. It is from Service Tree the information is retrieved on who the approvers are for the service or
subscription; without that information it's impossible to create exception requests or to authorize them.

Whitelisting a subscription, pre-authorize all deployments to such subscription, to all regions.

Get approval from FCM manager, or any other manager above FCM manager before whitelisting a subscription

## Execution instructions

1. Connect to **chggrd-api-sql-svr-prod.database.windows.net** server using SSMS.
    - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
    - Username and Password are available
      from [chggrd-api-kv-prod](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/8830ba56-a476-4d01-b6ac-d3ee790383dc/resourceGroups/chggrd-api-prod-westus2/providers/Microsoft.KeyVault/vaults/chggrd-api-kv-prod) secrets
        - Access to KeyVault requires JIT to **FcmProduction**
        - To access the secret you need to add yourself to the **Access Policies** of the Key Vault with permissions to **Get & List** Secrets
    - **chggrd-db-admin-username**
    - **chggrd-db-admin-password**
    - ![ssms](media/SSMS_prod_server.png)

> [!Note] **Make sure to remove your access policies from the Key Vault after you are done, else it will trigger s360 alerts.**

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