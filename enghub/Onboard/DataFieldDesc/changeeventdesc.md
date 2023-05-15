# Change Event Field Descriptions

| Field Name | Manditory? | Description | Remarks | Type | Triggers existing ChangeRecord update |
|:------------|:----------|:------------|:--------|:-----|:--------------------------------------|
| Source  | Yes  | Source system from where the record originates  | Provide the source system identity of the system. Contact FCM to register your Source before start sending change event.  | String  | N/A  |
| Title  | Yes  | A string that is meaningful to an engineer working with this application.  |    | String  | Yes  |
| Description  | Yes  | A string that is meaningful to an engineer working with this application.  |    | String  | No  |
| StartTime  | Yes  | When the change rollout started or will be started  | In UTC. See [DateTime Formatting](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/datetimeformatting)  | DateTimeOffset  | Yes  |
| StartTimeType  | Yes  | Actual Start time or Scheduled Start time  | Defined values: “Actual” “Scheduled”  | String  | Yes  |
| Priority  | Yes  | This is an enum value ranging from 1 to 4 with 1 being Highest Priority  |  Values: 1, 2, 3, 4  | Int  | Yesco  |
| ImpactedLocation  | Yes  | Location where change is impacted.  |  Location Name  | String  | Adds a new location  |
| LocationType  | Yes  | LocationType Values = AzureCluster, AzureDatacenter,  AzureRegion,  AzureLocation, Network device, Custom (for everything else)  | Even for multiple location in one change event it has to be of one Type. For multiple types multiple changeEvents need to be sent  | String  | N/A  |
| ImpactedServiceId  | Yes  | The Service for the change.   | Service GUID should be in Service Tree. maps to ServiceTreeId in FCM Service table  | String  | Yes  |
| ImpactedComponentId  | Optional  | The name of the software role, or physical device, or logical entity (e.g. VIP, VLAN) being changed.  | Component id should be in Service Tree. Maps to ComponentOid  | String  | Yes  |
| Status  | Yes  | Status of Change/Deployment  | For possible values see [Status Name Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/statusnamedesc) | String  | Yes  |
| SourceRecordId  | Yes  | A unique Id that represents this record in the source system. This need to be unique within the source.  | For ongoing change of the same event or entity user need to send the record with the same id  | String  | N/A  |
| ChangeType     | Yes  | Type of change  | For possible values see [Change Type Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/changetype)  | String/Int  | Yes  |
| EndTime  | Yes  | When the change rollout ended or will end  | In UTC see [Change Event Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/changeeventdesc)  | DateTimeOffset  | Yes  |
| EndTimeType  | Yes  | Actual End time or Scheduled End time  | Possible values: “Actual”, “Scheduled” | String  | Yes  |
| ChangeOwner  | No  | Change owner or change assigned to alias  | The alias has to be in AAD/IDWEB.  | String  | Yes  |
| BuildPath  | No  | Build Path  |  | String  | Yes  |
| BuildNumber  | No  | Build Number for the changed/deployment  |  | String  | Yes  |
| ChangeInitiator  | No  |  The initiator of the changed  |  | String  | Yes  |
| Created  | No  | When the change is created in the source system  | In UTC. See [DateTime Formatting](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/datetimeformatting)  | DateTimeOffset  | No  |
| EnvironmentName  | No  | Name of the environment where the change is done  | Specific list of allowed values.  See [Environment Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/environmentdesc)  | String  | Yes  |
| Modified  | No  | When the change is modified in the source system  |  In UTC. see [DateTime Formatting](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/datetimeformatting)  | DateTimeOffset  | Yes  |
| SubscriptionID  | No  | Subscription Id to which the change is associated (Need to be in ServiceTree)  | Azure Subscription id  | String  | Yes  |
| AppendDescription  | No  | If the description is going to be appended with the existing change   | boolean  | String  | N/A  |
| Risk  | No  | Risk associated with the change  | 1 (High), 2 (Medium), 3 (Low) | Int  | N/A  |
| ExternalSourceType  | No  | It might be applicable in few case where the external source type could be like Deployment/DeploymentTask etc.  |  | String  | No  |
| ExternalParentId  | No  | If the change event has a parent change id associated with it  | id for a changeRecord that already exists in FCM  | String  | Yes  |


