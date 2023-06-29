FCM in [Kusto​](https://aka.ms/kusto) enables engineers to answer ad hoc questions about their changes in FCM. The data is queryable via the Service GUIDs (from ServiceTree) for their Service.

## Access
The FCM Change events are in the Fcmdata kusto cluster, under the FCMKustoStore database in table ChangeEvent.

To view this data through the Kusto Explorer, please go to: https://fcmdataro.kusto.windows.net:443 and run the below query

<span style="font-family:Courier New; color:orange;">cluster('FCMDataro').database('FCMKustoStore').['ChangeEvent'] | limit 10</span>

## Change Event Schema

| Column Name | Data Type | Description |
|:------------|:----------|:------------|
| TIMESTAMP |datetime | Approximate time event was picked up by FCM |
| PreciseTimeStamp |datetime | Approximate time event was picked up by FCM |
| Tenant |string | Tenant ID |
| Role |string | |
| RoleInstance |string |  |
| Level |long |  |
| ProviderGuid |string |  |
| ProviderName |string |  |
| EventId |long |  |
| Pid |long |  |
| Tid |long |  |
| OpcodeName |string |  |
| KeywordName |string |  |
| TaskName |string |  |
| ChannelName |string |  |
| EventMessage |string |  |
| ActivityId |string |  |
| ActionName |string | Type of Change |
| ActualEnd |datetime |  |
| ActualStart |datetime |  |
| BuildNumber |string | Build Number for the changed/deployment  |
| BuildPath |string | Build Path  |
| ChangeRecordId |long |  |
| ChangeRecordParentId |long |  |
| ComponentName |string |  |
| Created |datetime | When the change is created in the source system  |
| Description |string | A string that is meaningful to an engineer working with this application.  |
| EndTime |datetime | When the change rollout ended or will end  |
| ExternalId |string | External change ID |
| ExternalSource |long |  |
| ExternalSourceName |string | Service used to deploy this change |
| MajorVersion |long |  |
| MinorVersion |long |  |
| Modified |datetime | When the change is modified in the source system  |
| Revision |long |  |
| ScheduledEnd |datetime |  |
| ScheduledStart |datetime |  |
| ServiceName |string |  |
| StartTime |datetime | When the change rollout started or will be started  |
| Status |string | Status of Change/Deployment  |
| SubscriptionId |string | Subscription Id to which the change is associated (Need to be in ServiceTree)  |
| TargetSwimLanes |string |  |
| Title |string | A string that is meaningful to an engineer working with this application.  |
| Locations |string |  |
| ServiceTreeGuid |string |  |
| SourceNamespace |string |  |
| SourceMoniker |string |  |
| SourceVersion |string |  |
| ExternalType |string |  |
| ExternalParentId |string | If the change event has a parent change id associated with it  |
| DeploymentTemplateName |string |

Additional schema information can be found in [Data Field Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/changeeventdesc)


<!-- Please refer to [FCM Architecture](https://eng.ms/docs/cloud-ai-platform/azure-core/one-fleet-platform/one-fleet-platform-timmall/federated-change-management/fcm-engineering-hub/onboard/doc2) for additional schema information -->

### Permissions
Request access to the FCM Users Security Group on http://idweb

### Data Retention
The ChangeEvent table supports the last 365 days of changes.

### Supported Use
The dataset is intended for exploration and answering ad hoc questions.
- Reporting should be done against the Kusto datastream​​ from the follower https://fcmdataro.kusto.windows.net:443/FCMKustoStore
- Service integration should be against the FCM APIs per agreed upon SLAs
- If you are seeing any of the Kusto limit errors while using 'Explore in lens' feature, please reduce the time window for which you are looking for data. Learn more here about [Query Limits](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/concepts/querylimits)

