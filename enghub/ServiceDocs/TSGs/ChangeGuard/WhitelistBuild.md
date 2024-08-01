# Whitelist a Build

## Overview

There might be cases where an Exception request cannot be created or approved due to certain reasons.

For these special cases we need a way to whitelist a entire build, so that all deployments to the specific service id, service group and build number are pre-authorized.

Whitelisting a build (ServiceId + ServiceGroupName + BuildNumber) pre-authorizes all deployments to all regions and subscriptions for that specific build.

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
   DECLARE @serviceId nvarchar(50);
   DECLARE @serviceGroupName nvarchar(256);
   DECLARE @buildNumber nvarchar(256);
   DECLARE @isEnabled bit;
   
   SET @serviceId = <<ServiceId>>;
   SET @serviceGroupName = <<ServiceGroupName>>;
   SET @buildNumber = <<BuildNumber>>;
   SET @isEnabled = 1;
   
   INSERT INTO [ServicesInfo].[WhitelistedBuilds]
   ( [ServiceId]
   , [ServiceGroupName]
   , [BuildNumber]
   , [IsEnabled])
   VALUES ( @serviceId
   , @serviceGroupName
   , @buildNumber
   , @isEnabled);

   ``` 
   >    [!NOTE]
   >    - Replace **«ServiceId»** with the service id value.
   >    - Replace **«ServiceGroupName»** with the service group name of the deployment.
   >    - Replace **«BuildNumber»** with the build number of the deployment.
