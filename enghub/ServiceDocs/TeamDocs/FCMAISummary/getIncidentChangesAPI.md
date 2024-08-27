# GetIncidentChanges API

## Overview
GetIncidentChanges API is an Azure Function that is currently called only by ICMEventProcessor (IEP). GetIncidentChanges API is responsible from:

1) Getting the search criteria for an incident by calling IncidentInformationProvider (IIP) and ServiceInformationProvider (SIP)
2) Given the search criteria from the IIP and SIP, calling Kusto to get changes that satisfy the search criteria.
3) Creating a deeplink to OneDeployFCM dashboard given the search criteria
4) Creating a text summary of the changes 
5) Returning the search criteria, text summary, changes and deeplink to OneDeployFCM dashboard as a response.


## Search Criteria

GetIncidentChanges API retrieves the search criteria for an incident from IIP. Search Criteria is an object as follows:

```json
{
    "StartTime": "datetime",
    "EndTime": "datetime",
    "ServiceId": "string",
    "ServiceName": "string",
    "SearchEntities": "string",
    "SearchEntityType": "string"
}
```

- EndTime here is the ImpactStartTime of the incident
- StartTime is currently `ImpactStartTime-12h`.
- ServiceId is the ServiceTreeId of the team who owns the incident at that given point in time.
- Currently we populate ServiceId and ServiceName field only if the search entity type is a region. You can find information on how we get search entities, and also which search entity types we support [here](https://eng.ms/docs/products/fcm-engineering-hub/icmchangeinsights/changeinsights).


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