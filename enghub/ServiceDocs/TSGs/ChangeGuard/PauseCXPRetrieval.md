# Pause CXP Retrieval

## Overview

The CXP Retrieval process updates/refreshes the database once the current date time is greater than the last update.  
Setting the last update value in the future pauses the refresh cycle until that moment.

## Execution instructions

1. Connect to **chggrd-api-sql-db-prod.database.windows.net** server using SSMS.
    - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
    - Username and Password are available
      from [chggrd-api-kv-prod](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/8830ba56-a476-4d01-b6ac-d3ee790383dc/resourceGroups/chggrd-api-prod-westus2/providers/Microsoft.KeyVault/vaults/chggrd-api-kv-prod) secrets (requires JIT
      to FcmProduction), under:
        - **chggrd-db-admin-username**
        - **chggrd-db-admin-password**

2. Once logged into SSMS, connect to **master** database and open the query window.
3. Run the following query:
   ``` 
      DECLARE @PauseUntil datetime2 = «date-here»; 
      DECLARE @LastUpdateId BIGINT = DATEDIFF_BIG( microsecond, '00010101', @PauseUntil ) * 10 + ( DATEPART( NANOSECOND, @PauseUntil ) % 1000 ) / 100;

      INSERT INTO [EventsRetrieval].[LastUpdate]
                 ([LastUpdateId] 
                 ,[LastUpdateDate]) 
           VALUES 
                 (@LastUpdateId 
                 ,@PauseUntil); 
   ```

   > [!NOTE]
   > - Replace **«date-here»** with the corresponding UTC time value.
   > - **@LastUpdateId** represents the number of ticks in **@PauseUntil**.
   >    - [many thanks to Michael J Swart](https://michaeljswart.com/2017/07/converting-from-datetime-to-ticks-using-sql-server)

