# Navigating Incidents That Involve Control Plane Changes

## What Types of Incidents Are Caused by Control Plane Changes?

- **CRUD Operation Failures** on VM or VMSS resources.

### Incident Pattern

- `ApiUnexpectedFailures` exceeded thresholds for `ApiName`: `virtualmachinescalesets.resourceoperation.put` in a specific region.

### Example of Control Plane Incidents

- [Incident-440639800](https://portal.microsofticm.com/imp/v3/incidents/incident/440639800/summary)
- [Incident-425736167](https://portal.microsofticm.com/imp/v3/incidents/incident/425736167/summary): CRUD operations failing for compute resources.

## How to Find Control Plane Changes

### Step 1: Select the `fabricCluster` as the EntityId

- **Get granular results by selecting `fabricCluster`.**
- If `fabricCluster` is not available, choose the region.

### Step 2: Identify the `fabricCluster` for a Given VM

- If you know the `VMId`, you can find the `fabricCluster` using the following Kusto query:

```kusto
cluster('azcrp.kusto.windows.net').database('crp_allprod').VMApiQosEvent
| where vMId == '<VMID>'
| project fabricCluster, PreciseTimeStamp
| order by PreciseTimeStamp desc
| limit 100
```

### Step 3: Use the Dashboard to Show Control Plane Changes

* **Go to the All Changes View** : [All Changes View]()
* **Reset Filters** : Ensure any pre-set filters are reset.
* **Enter `fabricCluster`** : Input the `fabricCluster` into the **EntityId** filter (e.g., `uswestcentral-prod-a`).
* **Set the Timeline** : Recommended to set the **Start Time** to 24 hours before the incident start time, as issues may be latent.

 **Dashboard Link** : [Control Plane Changes Dashboard]()
