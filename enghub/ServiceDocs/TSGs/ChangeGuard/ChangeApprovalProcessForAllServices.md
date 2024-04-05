# Onboard or remove an R2D service from the SafeFly approval process

## Overview

Change Guard was integrated with SafeFly to support the SafeFly approval process for certain onboarded services.

The current supported Approval Providers (Change Guard and SafeFly) are stored in the table `[ChangeApproval].[Providers]` in the Change Guard database.

The services onboarded to SafeFly and that go through the SafeFly approval process can be found in the Change Guard database in the table `[ChangeApproval].[ProviderSupportedServices]`.

In case we need to add or remove a service from the SafeFly approval process follow the instructions below. 

## Execution instructions

Add or remove a service from the SafeFly approval process by adding or removing/disabling a row in the
table `[ChangeApproval].[ProviderSupportedServices]`.

1. Connect to **chggrd-api-sql-db-prod.database.windows.net** server using SSMS.
    - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
    - Username and Password are available
      from [chggrd-api-kv-prod](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/8830ba56-a476-4d01-b6ac-d3ee790383dc/resourceGroups/chggrd-api-prod-westus2/providers/Microsoft.KeyVault/vaults/chggrd-api-kv-prod) secrets (requires JIT
      to FcmProduction), under:
        - **chggrd-db-admin-username**
        - **chggrd-db-admin-password**

2. Once logged into SSMS, connect to **chggrd-api-sql-db-prod** database and open the query window.
3. Run the following query to get the SafeFly provider id:
   ```
   DECLARE @SafeFlyId INT
   SELECT @SafeFlyId = P.Id
   FROM [ChangeApproval].[Providers] P
   WHERE P.Name = 'SafeFly'
   ``` 
4. Depending on the action you want to perform, run one of the following queries:
   1. To add a service to the SafeFly approval process:
      ``` 
      DECLARE @serviceId nvarchar(max);
      DECLARE @serviceName nvarchar(max);
      SET @serviceId = <<ServiceId>>;
      SET @serviceName = <<ServiceName>>;

      DECLARE @SafeFlyId INT;
      SELECT @SafeFlyId = <<SafeFlyId>>;
      
      INSERT INTO [ChangeApproval].[ProviderSupportedServices]
      ([ProviderId], [ServiceId], [ServiceName], [IsEnabled])
      VALUES (@SafeFlyId, @serviceId, @serviceName, 1 /* IsEnabled */)
      ```
   2. To remove a service from the SafeFly approval process you can either Disable it or Delete it; to disable it, run the following query:
      ```
      DECLARE @serviceId nvarchar(max);
      SET @serviceId = <<ServiceId>>;
      
      UPDATE [ChangeApproval].[ProviderSupportedServices]
      SET [IsEnabled] = 0 /* IsEnabled */
      WHERE [ServiceId] = @serviceId
      ```

>    [!NOTE]
>    - Replace **«ServiceId»** with the service id value.
>    - Replace **«ServiceName»** with the service name.
>    - Replace **«SafeFlyId»** with the id found during step 3.
