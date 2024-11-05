# Granting `write` access to SQL Database through JIT

## Overview

This document provides instructions on how to grant `write` access to the SQL Database for Change Guard.

To access the SQL Database you will need to use Entra ID authentication using your Microsoft (INT) or AME (PPE/ Prod) account.

Read access is already added to all members of the FCM and SafeFly teams. 

For write access, you will need to request access through JIT.

## Execution instructions
The write access to the SQL Database is granted through JIT. 

The steps to request access are as follows:
![JIT Details](media/JIT_SQL_Db.png)

#### The values for Production are:
- Server Name: chggrd-api-sql-svr-prod
- Subscription: 8830ba56-a476-4d01-b6ac-d3ee790383dc
- Location: westus2
- DB Name: chggrd-api-sql-db-prod
- Access level: db_owner

#### The values for PPE are:
- Server Name: chggrd-api-sql-svr-ppe
- Subscription: 6ac089d6-2695-4daf-95df-ea06d302b618
- Location: westus2
- DB Name: chggrd-api-sql-db-ppe
- Access level: db_owner

> [!NOTE]
> - There is also an auto-approve policy for the Change Guard DB db_datawriter access, for a Sev2 ICM.
> - For different access levels, replace **db_owner** with the new level value.
> - To be able to run Stored Procedures, you would need **db_owner** rights; for just write access use **db_datawriter**.
