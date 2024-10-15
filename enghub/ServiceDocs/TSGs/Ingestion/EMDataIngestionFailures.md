## EM Data Ingestion Failures Troubleshooting Guide

### Overview

We ingest significant amounts of data from the EMPlatform team for application and data deployments. There are primarily two jobs responsible for this data ingestion:

- [MapNodeUpgradesToEntityModel](https://kustoorchestrator-prod-web.azurewebsites.net/Manage/Details?cluster=Fcmdata&database=EntityModel&actorId=MapNodeUpgrades_ToEntityModel): Ingests data into the `EntityChangeEvents` table.
- [MapDataUpgradesToEntitymodel](https://kustoorchestrator-prod-web.azurewebsites.net/Manage/Details?cluster=Fcmdata&database=EntityModel&actorId=MapDataUpgrades_ToEntityModel): Ingests data into the `EntityChangeEvents_DataDeployments` table.

### Data Sources (Source column value in EntityChangeEvents Table)

The following source data are pulled by these jobs (source names start with):

1. OMRollout*
2. ScheduledEvent*
3. BatchingUpdate*
4. DERollout*
5. FDHERollout*
6. MaintenanceService*
7. RainerService*

### Troubleshooting Steps

If latency or change count monitors are triggered, follow these steps:

1. **Check Ingestion Failures:**
   - Verify if there are any ingestion failures for the two jobs mentioned above.
   - Troubleshoot based on the KO logs.

2. **Engage EM Team's DRI:**
   - If the above jobs are running fine, engage the EM Team's DRI (ICM Path: `OneDeploy/EntityModel`).
   - Use their dashboard - [EntityModel Monitoring](https://dataexplorer.azure.com/dashboards/0a6776f3-48ed-428b-a5ac-ab8a45bc5d28?p-_startTime=24hours&p-_endTime=now&p-_payload=all#95814a8e-750e-4989-8086-71c5cf886cca) to analyze if there is any failure on their end.