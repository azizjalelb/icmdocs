# Payload Standardization

We are standardizing the Payload format as we build new APIs to map the build to deployment and deployment to build. Currently, we are populating the payload/buildversion with the details we are receiving from Source System. 

Standardized Payload will contain the ServiceTreeGuid/ServiceGroupName and the BuildVersion/Payload we receive from source system. Standardization of Payload will be done when we ingest data into EntityChangeEvents Table.


## Current Payload Format from different Sources: 

| BuildVersion | Source |
|--------------|--------|
| 17.0.191 | AKSUnderlayNodeInfo |
| 16.0.5485.105-relms-3318196b | sqlmonrolloutprogress_infrastructureupgrades |
| v20240123.240125.1 | adorelease |
| 133503837041639839 | azdeployer |
|spm=spm_20086202311061_231115_115000|OMRollout.OrchestrationManagerTraceEvent


## Standardized Payload Format Examples:

|Source| Standardized PayloadFormat | Example |
|--|----------------------------|---------|
|ExpressV2 | ServiceTreeGuid/ServiceGroupName=BuildNumber | fe63f845-4aee-4313-9b2e-3a8a2fe61897/analyticsingestion=1.0.9.1265 |
|AzDeployer | ServiceTreeGuid=BuildNumber | 7a1b250d-eda8-4a74-918e-ca5fe0d0e9f8=5096320|
|PilotFish | ServiceTreeGuid=BuildNumber |1bd5fd01-0565-4c8e-affe-ec1b21c96529=5093666  |


In the first iteration of this work, we will be standardizing the payloads for 3 Source Systems - ExpressV2, AzDeployer and PilotFish and will explore other source systems in the next iterations.