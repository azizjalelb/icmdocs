# Payload Standardization

We are standardizing the Payload format as we build new APIs to map the build to deployment and deployment to build. Standardized payloads will help us to correlate the change across different orchestrators. 

Standardized Payload will contain the ServiceTreeGuid/ServiceGroupName and the Build Version/Payload we receive from source system. Standardization of Payload will be done when we ingest data into EntityChangeEvents Table. 

 

Standardized Payload Format: 


- For Below ARM– ServiceName or DataFolder = BuildVersion. 

- For Above ARM- ‘ServiceTreeGruid/Ev2ServiceGroupName = Buildversion’ 


## Standardized Payload Format Examples:

|Source| Standardized PayloadFormat | Example |
|--|----------------------------|---------|
|ExpressV2 | ServiceTreeGuid/ServiceGroupName=BuildNumber | fe63f845-4aee-4313-9b2e-3a8a2fe61897/analyticsingestion=1.0.9.1265 |
|PilotFish | Servicename=BuildNumber |hostconfigmanager=hcm_24_01_27_299   |
|PilotFish | DataFolder=BuildNumber |dataimage~amd64_prd=133526099359554534   |
|OMRollout | Servicename=BuildNumber |nicagent=nicagent_5_2_2_127   |


#### Note: 
In the above scenarios (both below and above ARM) the Service Name and ServiceGroupName are not ServiceTree concepts). For below ARM services ServiceName is the component that is being deployed/changes on the host. For above ARM services ServiceGroupName is the concept of EV2 and not the ServiceGroupName in the Service Tree 