# GetIncidentChanges API

## Overview
GetIncidentChanges API is an Azure Function that is currently called only by ICMEventProcessor (IEP). GetIncidentChanges API is responsible from:

1) Getting the search criteria for an incident by calling IncidentInformationProvider (IIP) and ServiceInformationProvider (SIP)

2) Given the search criteria from the IIP and SIP, calling Kusto to get changes that satisfy the search criteria.

3) Creating a deeplink to OneDeployFCM dashboard given the search criteria

4) Creating a text summary of the changes 

5) Returning the search criteria, text summary, changes and deeplink to OneDeployFCM dashboard as a response.


## Input Parameters:
| Parameter Name | Parameter Type | Parameter Description |
|----------------|----------------|-----------------------|
| IncidentId     | string         | The unique identifier of the incident |

## Output Parameters:
| Parameter Name | Parameter Type | Parameter Description |
|----------------|----------------|-----------------------|
| Summary        | string         | Summary of the changes found |
| SearchCriteria | IncidentSearchCriteria | Describes the criteria that is used when getting changes |
| Deeplink       | string    | Deeplink to OneDeployFCM dashboard for the changes found |
| ChangeEvents | List\<EntityChangeEventWithScores\> | List of changes we found |

Sample response would look like the following:

```json
{
    "Summary": "Found changes for locations cdm10prdapp01 between 2024-10-15 6:08:59 AM and 2024-10-15 6:08:59 PM",
    "SearchCriteria": {
        "startTime": "2024-10-15T06:08:59.47Z",
        "endTime": "2024-10-15T18:08:59.47Z",
        "serviceId": "",
        "serviceName": "",
        "searchEntities": "cdm10prdapp01",
        "searchEntityType": "cluster"
    },
    "ChangeEvents": [
        {
            "Rank": 1,
            "ScoringDetails": {
                "PayloadRiskScore": null,
                "CommonalityPercentage": null,
                "ProximityInMinutes": 2,
                "SafeflyRiskScore": ""
            },
            "ChangeActivity": "78548673-f42a-4dae-96d6-47fb52e6cce2$cdm10prdapp01",
            "Payload": "cosine\\activebranchflighting\\addvhdfiles;78548673-f42a-4dae-96d6-47fb52e6cce2",
            "EntityId": "cdm10prdapp01",
            "EntityType": "azurecluster",
            "ChangeType": "oaasrollout",
            "StartTime": "2024-10-15T18:06:16Z",
            "EndTime": "2024-10-15T18:07:56Z",
            "ChangeOwner": "rdos\\azure host os dri - sev 3-4",
            "IsImpactful": "false",
            "ReleaseUrl": "",
            "BuildUrl": "",
            "ImpactDuration": 0,
            "PlannedInterruption": "DiskImpact=None,ComputeImpact=None,NetworkImpact=None,OSImpact=None",
            "ImpactDetails": "{\"PlannedInterruption\":\"DiskImpact=None,ComputeImpact=None,NetworkImpact=None,OSImpact=None\",\"ImpactDuration\":0}",
            "SafeflyLink": "",
            "R2dId": "",
            "IsSFIRelated": "false"
        }
    ],
    "DeepLink": "https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2024-10-15T06:08:59.470Z&p-_endTime=2024-10-15T18:08:59.470Z&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=v-cdm10prdapp01&p-_serviceName=all&p-_entityType=all&p-_payload=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4"
}
```


### Incident Search Criteria

GetIncidentChanges API retrieves the search criteria for an incident from IIP. IncidentSearchCriteria is an object as follows:

```json
{
    "startTime": "datetime",
    "endTime": "datetime",
    "serviceId": "string",
    "serviceName": "string",
    "searchEntities": "string",
    "searchEntityType": "string"
}
```

- EndTime here is the ImpactStartTime of the incident
- StartTime is currently `ImpactStartTime-12h`.
- ServiceId is the ServiceTreeId of the team who owns the incident at that given point in time.
- Currently we populate ServiceId and ServiceName field only if the search entity type is a region. You can find information on how we get search entities, and also which search entity types we support [here](https://eng.ms/docs/products/fcm-engineering-hub/icmchangeinsights/changeinsights).


### EntityChangeEventScores
```json
{   
    "Rank": "int",
    "ScoringDetails": {
        "PayloadRiskScore:":"double",
        "CommonalityPercentage": "double",
        "ProximityInMinutes": "double",
        "SafeflyRiskScore": "string"
    },
    "ChangeActivity": "string",
    "Payload": "string",
    "EntityId": "string",
    "EntityType": "string",
    "ChangeType": "string",
    "StartTime": "DateTime",
    "EndTime": "DateTime",
    "ChangeOwner": "string",
    "IsImpactful": "string",
    "ReleaseUrl": "string",
    "BuildUrl": "string",
    "ImpactDuration": "long",
    "PlannedInterruption": "string",
    "ImpactDetails": "string",
    "SafeflyLink": "string",
    "R2dId": "string"
  }
```


## Calling Kusto to Get Changes

GetIncidentChanges API calls FCM Kusto cluster to get the changes that satisfy the search criteria for an incident. [GetChangesCopilot](https://msazure.visualstudio.com/DefaultCollection/One/_git/FCMAIChangeSummary?path=/FCMCopilot/Queries/GetChangesCopilot.kql) is the main kusto function that GetIncidentChanges API calls.

However, we are not calling our Kusto everytime there is a request to GetIncidentChanges API. We call our Kusto only if 
1) It has been less than 60 minutes since the ImpactStartTime of the incident.
2) If it has been more than 60 minutes since the ImpactStartTime of the incident, the search criteria must have been changed. The search criteria can change if the incident owning service changes or if the impacted location of the incident changes.
    - We keep track of whether the search criteria has changed or not by storing the SearchCriteria-ChangeSummary key-value pair in a Redis Cache after it has been more than 60 minutes since the ImpactStartTime of the incident. If we find a matching value in the Redis cache for the Search Criteria we get from IIP for an incident, we return the ChangeSummary value that we stored in the cache rather than calling Kusto to get changes again.


## Change Summary Scenarios

Based on the search criteria and whether we found changes or not, we are tweaking the summary text we return in the response. Currently, there are 4 scenarios:
1) **ChangesFoundSummaryWithService**: We found changes for given a search criteria and search criteria has ServiceId and ServiceName. 
2) **ChangesFoundSummaryWithOutService**: We found changes for given a search criteria and search criteria doesn't have ServiceId and ServiceName.
3) **NoChangeFoundSummaryWithService**: We didn't find changes for given a search criteria and search criteria has ServiceId and ServiceName. 
4) **NoChangeFoundSummaryWithOutService**: We didn't find changes for given a search criteria and search criteria doesn't have ServiceId and ServiceName.