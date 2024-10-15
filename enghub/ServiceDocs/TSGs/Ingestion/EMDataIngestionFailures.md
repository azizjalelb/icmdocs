## EM Data Ingestion Failures Troubleshooting Guide

### Overview

We ingest significant amounts of data from the EMPlatform team for application and data deployments. There are primarily two jobs responsible for this data ingestion:

- [MapNodeUpgradesToEntityModel](https://kustoorchestrator-prod-web.azurewebsites.net/Manage/Details?cluster=Fcmdata&database=EntityModel&actorId=MapNodeUpgrades_ToEntityModel): Ingests data into the `EntityChangeEvents` table.
- [MapDataUpgradesToEntitymodel](https://kustoorchestrator-prod-web.azurewebsites.net/Manage/Details?cluster=Fcmdata&database=EntityModel&actorId=MapDataUpgrades_ToEntityModel): Ingests data into the `EntityChangeEvents_DataDeployments` table.

### Data Sources (Source column value in EntityChangeEvents Table)

The following sources data are pulled by the above two jobs (source names start with):

1. OMRollout*
2. ScheduledEvent*
3. BatchingUpdate*
4. DERollout*
5. FDHERollout*
6. MaintenanceService*
7. RainerService*

### Source cluster details
1. [MapNodeUpgradesToEntityModel](https://msazure.visualstudio.com/One/_git/FCM-DataPlatform?path=/src/Kusto%20Scripts/EntityModel/Functions/Ingestion/NodeChanges/Ingestion/MapNodeUpgrades_ToEntityModel.kql) - This job uses two clusters
    - cluster('azdeployerfollower.eastus.kusto.windows.net').database('AzDeployerKusto').RTOAuditEvent 
    - cluster('emplatform.westus.kusto.windows.net').database('EntityModel').fEntityChangeEventsV2 
2. MapDataUpgradesToEntitymodel - This job pulls data from the emplatform itself but uses a different cluster
    - cluster('emplatformsecondaryflr.centralus.kusto.windows.net').database('EntityModel').fEntityChangeEventsV2_DataDeployments

### Source Cluster Access
Our team should have access by default as EM team has granted viewere access to 'Scott Guthrie's Organization (FTE)' group.

### Troubleshooting Steps

If latency or change count monitors are triggered, follow these steps:

1. **Check Ingestion Failures:**
   - Verify if there are any ingestion failures for the two jobs mentioned above.
   - Troubleshoot based on the [KO logs](https://dataexplorer.azure.com/clusters/fcmdata/databases/EntityModel?query=H4sIAAAAAAAAA6VU30%2FbQAx%2B71%2Fh9eVa1EH59dKpk8YoUgUMRuFpTMhc3PS25C7zXWgz7Y%2Bf09I0AQST1pc6Z3%2BffZ%2FtSyhAhozpJx3MgwnFOIIhqHPMvriIbrKYMSJ%2Fd%2B1GNoj3XA4T9aGVVLAsG1sf0GoqcVO8Z6MHO6cX2yc6jTDg%2Bybw9OLuzMWtPzCfEVML5NegGD6nRRst487ogRJ4J1nGduo4xWCcVZX7kkkbT9cmpUnANIOPgLHr7EbdKuScvMeY4J12NqCxHtQJmoQiCA5oQToPBGFGwPQrJx%2FA51oLZponSQE4DcTiCmzIb6vXWHM7E29JzJQaGxG%2FGn5FMVliDDRaBLLhqDhmlx0V1xir1s4OnAjFsq5Nk0RBEcoT%2FCx9Q8kT0wKmCcZevm5MlWZuwgy21Ph4AKqG3wU1ULBV0TwJb28i24N2HbgHqr0CUllrBI3B0Q4T8po6tUy9Orq7bn0DN3w2g45Bmplmoeg8cXUbihCzhKar6t8Q5ckl20zonRVd2jBaaMrKeRJdvg1u%2BdZ%2Br6vzb3wVSZNy70XKBraK3Qc1CVKXDE38NScuSpkc%2F1cttVIO3i5lS4nsKDurV9qWYzN5PBktxVYlwSOe3Q%2FSodbLHlyWnFG5VznTmnooq3TvZXNs3KlmpEHbq%2FWgZu%2FV7P2afdBbl93tQb8Hu4d9MWrPRuUfbjI%2FniwBh%2F1%2BfzlKk5mbb0bJg3ccZHHvC3Ba58wkZHJVn6cpsvlN8NnlNixnXf47kvUK58%2Bui7ZYp%2BuWXC%2BpIqyO5W0o%2FStSeWr1XzaVxySSBQAA)

2. **Zero Change Count:**
    - If the Zero Change Count monitor is triggered, get the Source Name from the incident and verify in the emplatform cluster if the data is available.
    - If the data is not available for the given time period in the EMPlatform cluster as well, then follow step #3
    - If the data is avaialable in the Source(emplatform) but is not available in our Kusto, then verify if there is any issues on the KO Job running.

3. **Engage EM Team's DRI:**
   - If the above jobs are running fine, engage the EM Team's DRI (ICM Path: `OneDeploy/EntityModel`).
   - Use their dashboard - [EntityModel Monitoring](https://dataexplorer.azure.com/dashboards/0a6776f3-48ed-428b-a5ac-ab8a45bc5d28?p-_startTime=24hours&p-_endTime=now&p-_payload=all#95814a8e-750e-4989-8086-71c5cf886cca) to analyze if there is any failure on their end.

4. **Latency Issues:**
    - If the latency monitors get triggered, then follow the [Data Latency guide](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/ingestion/investigatehighdataingestionlatency).