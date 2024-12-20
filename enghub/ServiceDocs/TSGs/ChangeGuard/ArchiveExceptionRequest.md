﻿# Archive an Exception Request

## Overview

Change Guard avoids duplicate ExceptionRequests as much as possible; where the definition of a duplicate exception is one that is for the same service, subscriptions, and regions as one already created.

So, ChangeGuard will not let you create another ExceptionRequest if the request is for the same service, the same subscriptions or a subset of the then, and the same regions or s subset of them.

There had been cases where an exception request was created and afterwards the requester notices the exception request doesn't include the needed approver.

The requester gets the approver added in ServiceTree ChangeGuard metadata, tries to create a new exception request that includes the newly added approver but it only gets back the old exception request.

This is one case when you archive an exception request. 

## Execution instructions

1. Connect to **chggrd-api-sql-svr-prod.database.windows.net** server using SSMS.
    - If SSMS not installed in your computer, see: [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
    - Use Entra Authentication along with your `@ame.gbl` account to connect to the server.
        - ![ssms](media/SSMS_prod_server.png)
    - To get write access to the SQL Database, see: [Granting `write` access to SQL Database through JIT](JITAccessToSQLDatabase.md)

2. Once logged into SSMS, connect to **chggrd-api-sql-db-prod** database and open the query window.
3. Run the following query:
   - ``` exec [dbo].[DeleteExceptionRequest] '<ExceptionrequestId>','<DeletedByAlias>',' <reason, provide mail or incidentid>' ``` 