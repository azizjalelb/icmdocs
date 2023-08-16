# SDK Ingestion Resources Deployment using Region Agnostic Model

THIS PAGE IS "WORK IN PROGRESS"

This document guides the developer to deploy sdk ingestion resources in multiple environments. There are several steps in this process,some automated and some are manual.

### Step 1
Stage map should be deployed manually before running the release pipeline, this is the only required manual step.

Set variables used in the command:

#### Examples for INT environment:

    $stageMapAbsolutePath = '..\EngSys-ChangeManagement-FCM\src\FCM\RegionAgnosticModelNew\StageMap.json'
    $serviceIdentifier  = '889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f'
    $serviceGroup = "Microsoft.Azure.FederatedChangeManagement"
    $rolloutInfra = "Prod" //this is just temporary until ev2 team fixes the environmnet dropdown in the release pipeline definition

Deploy stagemap using the following command:

    New-AzureServiceStageMap -StageMapFilePath $stageMapAbsolutePath -ServiceIdentifier $serviceIdentifier -ServiceGroup $serviceGroup -RolloutInfra $rolloutInfra

### Step 2 

Run release pipeline: [Link to Release Pipeline](
https://msazure.visualstudio.com/One/_release?definitionId=51803&view=mine&_a=releases)

Monitor rollout progress:   https://ra.ev2portal.azure.net/

### The following resources are deployed during the rollout together with their resource groups:

    1. Key Vault, secrets and certificates used by other resources
    2. Event Hub
    3. storage Account
    4. Traffic Manager
    4. Dns Zone
    5. Azure Data Explorer
    6. Sql database
    7. Shard Sql Database
    8. Standard Connector
    9. Custom Connector
    10. Web Api Read
    11. Web Api Write

## Steps to deploy the region agnostic model using PowerShell

#### Set runtime variables accordingly
	$serviceGroupRoot = '...\EngSys-ChangeManagement-FCM\src\FCM\RegionAgnosticModelNew'
	$rolloutInfra = ''
	$stageMapAbsolutePath = '...\EngSys-ChangeManagement-FCM\src\FCM\RegionAgnosticModelNew\StageMap.json'
	$serviceIdentifier  = ''
	$serviceGroup = ''
	$stageMapName = ''
	$selectRegionsForRollout = 'regions(eastus,westus)'
	$generatedVersion = '1.0.0'

#### Register StageMap
	New-AzureServiceStageMap -StageMapFilePath $stageMapAbsolutePath -ServiceIdentifier $serviceIdentifier -ServiceGroup $serviceGroup -RolloutInfra $rolloutInfra
#### Register ServiceArtifacts located in $serviceGroupRoot directory
	Register-AzureServiceArtifacts -ServiceGroupRoot $serviceGroupRoot  -ServiceGroupOverride $serviceGroup -RolloutSpec "RolloutSpec.json" -RolloutInfra $rolloutInfra -Force
#### Start Azure Service Rollout
	New-AzureServiceRollout -ServiceIdentifier $serviceIdentifier -ServiceGroup $serviceGroup -StageMapname $stageMapName -Select $selectRegionsForRollout -ArtifactsVersion $generatedVersion -RolloutInfra $rolloutInfra


#### Use this command to unregister the ServiceArtifacts 
	Unregister-AzureServiceArtifacts -ServiceGroup $serviceGroup -ServiceIdentifier $serviceIdentifier -RolloutInfra Test -ConfirmDelete

* [Link to demo repository](https://msazure.visualstudio.com/Azure-Express/_git/Samples?path=/RegionAgnostic_Rollout_Preview/src/ServiceGroupRoot/ServiceModel.json&version=GBmaster)

* [Ev2 Docs For Region Agnostic](https://ev2docs.azure.net/features/buildout/genericServiceModel.html?q=serviceMetadata) 

#### Sample values used for INT deployment

	$serviceGroupRoot = 'C:\work\projects\EngSys-ChangeManagement-FCM\src\FCM\RegionAgnosticModelNew'
	$rolloutInfra = 'Test'
	$stageMapAbsolutePath = 'C:\work\projects\EngSys-ChangeManagement-FCM\src\FCM\RegionAgnosticModelNew\StageMap.json'
	$serviceIdentifier  = '889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f'
	$serviceGroup = "Microsoft.Azure.FederatedChangeManagement"
	$stageMapName = 'TestName'
	$selectRegionsForRollout = 'regions(eastus,westus)'
	$generatedVersion = '1.0.0'


### Post Deployment Steps

    1. Dns Zone configuration should be done manually
    2. Secret values should be updated accordingly


### Steps to test the deployment
    Section to be filled later...