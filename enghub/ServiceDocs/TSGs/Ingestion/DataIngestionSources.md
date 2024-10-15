# List of Data Sources

## Data Ingestion Sources for EntityModel

| Source/Functionality | Cluster Information | Contact | ICM Team Path |
|----------------------|---------------------|---------|---------------|
| AKS | `cluster('AKS').database('AKSprod')`<br>`cluster('akshuba.centralus.kusto.windows.net').database('AKSinfra').UnderlayNodeInfo`<br>`cluster('aksinfra.centralus.kusto.windows.net').database('AKSinfra').UnderlayNodeInfo` | Cameron Childress | |
| CosmosDB | `cluster('cdbsupport.kusto.windows.net').database('Support').Upgrades(completed=completedFalse, federation=federation, useBestEffort=useBestEffort)`<br>`cluster('cdbsupport.kusto.windows.net').database('Support').UpgradeOperations()` | Ramana Prakash Kavi | Azure Cosmos DB/Deployment on-call |
| FUSE | `cluster('azwan.kusto.windows.net').database('FUSE').FUSE` | Shanim Sainul Abdeen, Mauricio Tsugawa, anfuseteam@microsoft.com | |
| SQL | All SQL clusters. Please refer to the kusto function:<br>`GetMonAnalyticsDBSnapshot_Staging` | yishuxu@microsoft.com,<br> nehabashyam@microsoft.com,<br>mohamed.elhassouni@microsoft.com | |
| Anvil Repairs | `cluster('aplat.westcentralus.kusto.windows.net').database('APlat').AnvilRepairServiceForgeEvents`<br>`cluster('aplat.westcentralus.kusto.windows.net').database('APlat').AnvilRepairServiceRequestSnapshot` | Travis Jensen, Binit Mishra | |
| APIM | `cluster('apimnortheurope.northeurope.kusto.windows.net').database('APIMProd').Orchestration`<br>`cluster('apim.kusto.windows.net').database('APIMProd').Orchestration` | Shilpa Mani, Kedar Joshi | API Management/ServicingLoop |
| App Services | `cluster(wawswus).database("wawsprod").AntaresCloudDeploymentEvents`<br>`cluster(wawseus).database("wawsprod").AntaresCloudDeploymentEvents`<br>`cluster(wawscus).database("wawsprod").AntaresCloudDeploymentEvents` | Shivam Rawat, Karl Reinsch, Petr Podhorsky | |
| Az Deployer | `cluster('azdeployerfollower.eastus.kusto.windows.net').database('AzDeployerKusto').DeploymentAuditEvent`<br>`cluster('azdeployerfollower.eastus.kusto.windows.net').database('AzDeployerKusto').RTOAuditEvent` | Mayank Meghwanshi | OneDeploy/AzDeployer |
| B2P | `cluster('1es').database('AzureDevOps').BuildArtifact` | aka.ms/cloudmine | |
| Entity Risk Score | `cluster('emplatform.westus').database('EntityModel').fEntityRiskScore_HighRisk` | Sunil | |
| Express Route | `cluster('hybridnetworking.kusto.windows.net').database('aznwmds').GatewayTenantHealth` | Rachel Chu | Cloudnet\ExpressRoute |
| MDM | `cluster('geneva.kusto.windows.net').database('genevadb').GetMetricsManifestMetadata()` | Sam Kennan, Elise Gale | Geneva Monitoring\Release Management |
| NodeDataUpgrades | `cluster('emplatform.westus.kusto.windows.net').database('EntityModel').fEntityChangeEventsV2_DataDeployments` | Sunil | OneDeploy/EntityModel |
| NodeUpgrades | `cluster('azdeployerfollower.eastus.kusto.windows.net').database('AzDeployerKusto').RTOAuditEvent`<br>`cluster('emplatform.westus.kusto.windows.net').database('EntityModel').fEntityChangeEventsV2` | Sunil, Prawal | |
| RedisCache | `cluster('DdazureServices').database('DDAzureServicesApps').RedisCache_ControlPlane_V2` | leiding@microsoft.com | |
| ServiceBus | `cluster('azuremessaging').database('MessagingRuntimeLogs').DeploymentUpgradeHistory` | Shankar Reddy Sama | |
| SafeFlyRequest | `cluster('safeflycluster.westus.kusto.windows.net').database('safefly').SafeFlyRequestArchive`<br>`cluster('safeflycluster.westus.kusto.windows.net').database('safefly').SafeFlyRequest` | Richa Singh, Swati Rashmi | Az core quality Engineering/Safefly |
| AzDM Changes | `cluster('azcpplatform.westcentralus.kusto.windows.net').database('AzCPPlatform')` | Mark Mccasey | |


## Data Ingestion Sources for FCMKustoStore

| Source/Functionality | Cluster Information | Contact | ICM Team Path |
|----------------------|---------------------|---------|---------------|
| ExpressV2 | `cluster('admcluster.kusto.windows.net').database('ADMDatabase')`<br>`cluster('admcluster.kusto.windows.net').database('ADMFFDatabase')`<br>`cluster('admcluster.kusto.windows.net').database('ADMMCDatabase')` | Pradeep Narayan |  onedeploy/Azure Service Deploy (Express v2) |
| Xstore-WADI | `cluster('dedata.kusto.windows.net').database('actionhistory')` | Keneth Ma |  OneDeploy/WADI |
| Xstore-XDS | `cluster('xdiagnostics.westcentralus.kusto.windows.net').database('xdiagnostics')` | David Ho |  Xstore/Kusto Infrastructure |
| Geneva Actions | `cluster('genevaactions.kusto.windows.net').database('Production').Audit`<br>`cluster('genevaactions.kusto.windows.net').database('Production').Extensions` | Ravi Prakash | Geneva Monitoring/Geneva Actions |
| AzDeployer | `cluster('azdeployerfollower.eastus.kusto.windows.net').database('AzDeployerKusto')` | Mayank Meghwanshi/Prawal Agarwal | OneDeploy/AzDeployer |
| Fuse Changes | `cluster('azwan.kusto.windows.net').database('FUSE')` | Shanim Sainul Abdeen, Mauricio Tsugawa, anfuseteam@microsoft.com | |
| GetRolloutLabels | `cluster('azurecm.kusto.windows.net').database('AzureCM')` | Mark Mccasey, azcdata@microsoft.com |  |