# Analysis of DataPlatform APIs on Azure Declared Outages

## Results

- Incidents need either:
  - Granular locations (`node`, `cluster`, `storagetenant`, etc.) in the ticket to be resolved for ranking changes to be enabled since we currently only support the above three entity types.
  - Resolve the serviceTreeId successfully from IcmTS (this is a bug currently being fixed).
  - We can also enable ranked changes on `region` type entities by adding some validation logic in the backend, though this would require some though.

I think the pieces are there to retrieve ranked changes but Icm tickets need better input from the customer to be useful. 

## Appendix

### Incident: 439326788

- Link: https://portal.microsofticm.com/imp/v3/outages/details/439326788/overview
- Params:
  - Location: md-dr2ndbkrq000 (storage account)
  - Service: Xstore ()
  - Time: 2023-11-06 21:00 PST - 2023-11-07 18:55 PST
  - Status: MITIGATED
  - Notes: Can't use the location since it doesn't show up in LIP, we would need to resolve this type of location (storage account).


Request Body:

```
{
    "ServiceTreeIds": [
        "734379f9-2d2c-48d4-a52a-5c509f699de4",
    ],
    "startTime": "2023-11-06T21:00:00.000Z",
    "endTime": "2023-11-07T18:55:27.874Z",
    "entities": [],
    "sortBy": "ranking",
    "sources": [],
    "changeTypes": [],
    "payloads": []
    "changeActivities": []
}
```

Result: We are getting results back but none of them have weighted scores due to no location + no found builds with EntityRiskScores.

### Incident 411292783

- Link: https://portal.microsofticm.com/imp/v3/incidents/incident/411292783/summary
- Params:
  - Location: East Us
  - Service: Azure Allocator
  - Time: 2023-08-01 15:39:00 PDT  - 2023-08-01 17:00:00 PDT
  - Status: Resolved
  - Notes: Part of DRF forum.

Request Body:

```
    "ServiceTreeIds": [
        "d292201e-3a06-46e4-85e8-258e04a3921f",
    ],
    "startTime": "2023-08-01 7:39:00",
    "endTime": "2023-08-01 9:00:00",
    "entities": [{'EntityType': 'region', 'EntityId': 'east us'}],
    "sortBy": "ranking",
    "sources": [],
    "changeTypes": [],
    "payloads": []
    "changeActivities": []

```

Result: 400 BadRequest, not able to run this type of query since we don't support the EntityType `region` for ranking changes. 

### Incident: 426949810

- Link:
- Params:
  - Location: asiaeast-prod-a	
  - Service: https://portal.microsofticm.com/imp/v3/outages/details/426949810/overview
  - Time: 2023-09-26 22:59:00 PDT - 2023-09-27 12:16:00 PDT
  - Status: MITIGATED
  - Notes: Part of DRF forum.


Request Body:

```
    "ServiceTreeIds": [],
    "startTime": "2023-09-26 22:59:00" ,
    "endTime": "2023-09-27 12:16:00",
    "entities": [],
    "sortBy": "ranking",
    "sources": [],
    "changeTypes": [],
    "payloads": []
    "changeActivities": []
```

Result: We receive a 400 Bad Request since we can't resolve either the location (asiaeaest-prod-a) or a service (neither Compute Manager or Blackbird). 

### Incident: 440722942

- Link: https://portal.microsofticm.com/imp/v3/outages/details/440722942/overview
- Params:
  - Location: east us, east us 2, central us, north central use
  - Service: ace8d53f-889a-488c-9cc9-d31fb4bbc84a
  - Time: 2023-11-10 23:56 PDT - 2023-11-11 01:40 PST
  - Status: MITIGATED
  - Notes: Part of Azure outage


Request Body:

```
    "ServiceTreeIds": ["ace8d53f-889a-488c-9cc9-d31fb4bbc84a"],
    "startTime": "2023-09-26 22:59:00" ,
    "endTime": "2023-09-27 12:16:00",
    "entities": [{'EntityType': 'region', 'EntityId': 'east us'}, {'EntityType': 'region': 'entityId': 'east us 2'}, {'EntityType': 'region', 'EntityId': 'central us'}, {'EntityType': 'region', 'EntityId': 'north central us'}],
    "sortBy": "ranking",
    "sources": [],
    "changeTypes": [],
    "payloads": []
    "changeActivities": []
```

Result: Result: 400 BadRequest, not able to run this type of query since we don't support the EntityType `region` for ranking changes. We are able to run the query for service name though and get a span search of changes. I think we should remove the `region` qualifier.

### Incident: 425736167

- Link: https://portal.microsofticm.com/imp/v3/outages/details/425736167/overview
- Params:
  - Service: bc592c9b-c702-4c43-9c7e-d0309f53435b
  - Location:  chinanorth
  - Time: 2023-09-21T19:45:00Z - 2023-09-22T19:45:00Z
  - Status: Resolved
  - Notes: Part of DRF forum.

Request Body:

```
    "ServiceTreeIds": ["bc592c9b-c702-4c43-9c7e-d0309f53435b"],
    "startTime": "2023-09-21T19:45:00Z" ,
    "endTime": "2023-09-22T19:45:00Z",
    "entities": [{'EntityType': 'region', 'EntityId': 'china north'}],
    "sortBy": "ranking",
    "sources": [],
    "changeTypes": [],
    "payloads": []
    "changeActivities": []
```

400 BadRequest, not able to run this type of query since we don't support the EntityType `region` for ranking changes. 