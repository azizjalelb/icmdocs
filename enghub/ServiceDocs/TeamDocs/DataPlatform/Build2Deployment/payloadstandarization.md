# Payload Standardization

We are standardizing the Payload format as we build new APIs to map the build to deployment and deployment to build. Standardized payloads will help us to correlate the change across different orchestrators. 

Standardized Payload will contain the ServiceTreeGuid/ServiceGroupName and the Build Version/Payload we receive from source system. Standardization of Payload will be done when we ingest data into EntityChangeEvents Table. 

 

Standardized Payload Format: 


- For AzDeployer  
    - It has only App Deployments. Standard format will be 'ServiceName = BuildVersion’ 

- For PilotFish – There are three types of deployments 

    - Configuration changes, Standard format will be ‘DataFolder = BuildVersion’
    - Data Deployments, standard format will be ‘DataFolder = BuildVersion’
    - App Deployments, standard format will be ‘ServiceName = BuildVersion’

- For EV2 - ‘ServiceTreeGruid/Ev2ServiceGroupName = Buildversion’ 

- For node level changes we are receiving from EM, we are receiving the payload in standard format. i.e. ‘ServiceName = BuildVersion’


## Standardized Payload Format Examples:

|Source| Standardized PayloadFormat | Example |
|--|----------------------------|---------|
|ExpressV2 | ServiceTreeGuid/ServiceGroupName=BuildNumber | fe63f845-4aee-4313-9b2e-3a8a2fe61897/analyticsingestion=1.0.9.1265 |
|AzDeployer | Servicename=BuildNumber | slbhostplugin=slbhp_90f060a9_11752060_12-0-1793-0 |
|PilotFish | Servicename=BuildNumber |network resource provider =5093666   |


#### Note: 
In the above scenarios (both below and above ARM) the Service Name and ServiceGroupName are not ServiceTree concepts). For below ARM services ServiceName is the component that is being deployed/changes on the host. For above ARM services ServiceGroupName is the concept of EV2 and not the ServiceGroupName in the Service Tree 