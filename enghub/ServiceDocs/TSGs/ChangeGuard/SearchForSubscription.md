# Search for Subscription

## Overview

Change Guard syncs subscription data from Service Tree using a Lens Orchestrator job that runs every 10 minutes.
There are times when a rollout will both build a new subscription and try to deploy resource to it.
If the subscription is newly created and the sync didn't run yet, it will not be found in our system.

To check if a subscription is available in our system, follow the instructions below.

## Execution instructions

1. Connect to **chggrd-api-sql-svr-prod.database.windows.net** server using SSMS.
   - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
   - Use Entra Authentication along with your `@ame.gbl` account to connect to the server.
      - ![ssms](media/SSMS_prod_server.png)
   - To get write access to the SQL Database, see: [Granting `write` access to SQL Database through JIT](JITAccessToSQLDatabase.md)

2. Once logged into SSMS, connect to **chggrd-api-sql-db-prod** database and open the query window.
3. Run the following query:
    - ``` exec [sp_FindSubscription] '<<SubscriptionId>>' ```