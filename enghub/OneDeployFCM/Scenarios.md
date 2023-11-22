<h1>Examples/ Scenarios: </h1>

### <a name="navigatingControlPlaneChanges"> <h2>Navigating Incidents that involve Control Plane Changes </h2> </a>

**What type of Incidents are caused by Control Plane Changes?**

CRUD operation failures on VM, VMSS 

**Incident pattern** - ApiUnexpectedFailures exceeded thresholds for ApiName: virtualmachinescalesets.resourceoperation.put. Location: < Region >. 

Example of Control plane Incident: [Incident-440639800 Details - IcM (microsofticm.com)](https://portal.microsofticm.com/imp/v3/incidents/incident/440639800/summary) 

OR [Incident 425736167](https://portal.microsofticm.com/imp/v3/incidents/incident/425736167/summary) : CRUD operations failing for compute resources in …. 


### <a name="controlPlaneChanges"> **How to find Control plane changes?** </a>

Select the fabricCluster as the EntityId to get granular results 

If fabriccluster is not available, choose the region 

**How to Identify fabricCluster for a given VM?**

If you know the VMId, you can find the fabric cluster using the query  

```
cluster('azcrp.kusto.windows.net').database('crp_allprod').VMApiQosEvent
| where vMId =='<VMID>'
| project fabricCluster,PreciseTimeStamp
| order by PreciseTimeStamp desc
| limit 100
```

**Where and what input is given in the dashboard to show the control plane changes?**

Identify the fabric cluster: uswestcentral-prod-a (provided in the incident 440639800) 

Identify control plane changes: 

1. Go to Change Details view  [FCM (azure.com)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 

2. Make sure you remove/reset any filters, already set 

3. Enter the fabric cluster in to EntityId: uswestcentral-prod-a 

4. Enter the above fabric cluster name in the EntityId filter and set the time line correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so set the time filters as needed. 


<img src="media/changeDetailsAllUpdates.png" alt="alt text" width="1000"/>

Dashboard link: [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-11-09T23-51-00Z&p-_endTime=2023-11-10T23-51-00Z&p-_entityIds=v-uswestcentral-prod-a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 


### <a name="networkingChanges"> <h2>Navigating Incidents that involve Networking Changes </h2> </a>

**What type of Incidents are caused by SDN Changes?**

Network latencies, lost connection with the VM, lost connection between compute and storage nodes

**Example of SDN  Incident:**

[Incident-425027989 Details - IcM (microsofticm.com)](https://portal.microsofticm.com/imp/v3/incidents/details/425027989/home), The Host updates (NMAgent ) has triggered query time outs, followed by more issues on the client side

**Where and what is the input given in the dashboard to show the SDN (software defined network) changes**

The first step in identifying the host updates is to identify the node or cluster or storage tenant/cluster. In the above incident, the below Entities/locations are identified

**Storage Nodes:** 222038fd-8e2a-4232-9c53-e4d1144312af, 3206df73-7121-480a-9bf3-65169887a5d1, 9ded79f9-5971-4b61-a187-7b05d0d425e4

**Storage Tenant:** ms-hkg21prdstf01a

**Storage Cluster:** hkg21prdstf01

If granular location is provided, then the number of changes will be confined, correlated and accurate. It is highly recommended to inputs node’s affected to get accurate results. 

**Changes for Nodes:** 

1. Go to [Node View](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_nodeid=all&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43)
2. Get the nodes affected in the comma separated format, in this case 222038fd-8e2a-4232-9c53-e4d1144312af, 3206df73-7121-480a-9bf3-65169887a5d1, 9ded79f9-5971-4b61-a187-7b05d0d425e4 
3. Enter the above comma separated values into NodeId filter and set the time line correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so set the time filters as needed. 

<img src="media/nodeViewNetwoking.png" alt="alt text" width="1000"/>

Dashboard link : [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-09-19T11-56-00Z&p-_endTime=2023-09-20T11-56-00Z&p-_nodeid=v-222038fd-8e2a-4232-9c53-e4d1144312af%2C+3206df73-7121-480a-9bf3-65169887a5d1%2C+9ded79f9-5971-4b61-a187-7b05d0d425e4&p-_dynamicMeasure=all&p-_entityTypeNode=v-node#08c31477-dfa3-43d3-9427-a6a57b228c43) 

**Changes for StorageTenant:**

1. Go to Change Details view  [FCM (azure.com)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 

2. Make sure you remove/reset any filters, already set 

3. Enter the storage tenant in EntityId : ms-hkg21prdstf01a 

4. Enter the above SQL cluster name in the EntityId filter and set the time line correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so set the time filters as needed. 

<img src="media/changeDetailsST.png" alt="alt text" width="1000"/>

Dashboard link : [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-09-19T11-56-00Z&p-_endTime=2023-09-20T11-56-00Z&p-_entityIds=v-ms-hkg21prdstf01a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 

**Changes for Cluster:** 

1. Go to Change Details view  [FCM (azure.com)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 
2. Make sure you remove/reset any filters, already set 
3. Enter the Cluster in Cluster filter: hkg21prdstf01 
4. Enter the above SQL cluster name in the EntityId filter and set the timeline correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so se the time filters as needed. 

<img src="media/changeDetailsCluster.png" alt="alt text" width="1000"/>

Dashboard link : [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-09-19T11-56-00Z&p-_endTime=2023-09-20T11-56-00Z&p-_entityIds=v-ms-hkg21prdstf01a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 


### <a name="storageChanges"> <h2>SQL reports that a tenant is unhealthy and needs to investigate potential host- related culprits: </h2> </a>

Identify Changes made to SQL cluster, For example incident [429061332](https://portal.microsofticm.com/imp/v3/incidents/incident/429061332/summary)

SQL cluster: tr21509.eastus2-a.worker.database.windows.net 

**Changes for SQL Cluster:** 

1. Go to Change Details view  [FCM (azure.com)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 

2. Make sure you remove/reset any filters, already set 

3. Get the SQL cluster : tr21509.eastus2-a.worker.database.windows.net 

4. Enter the above SQL cluster name in the EntityId filter and set the time line correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so se the time filters as needed. 

<img src="media/changeDetailsSQL.png" alt="alt text" width="1000"/>

Dashboard Link : [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-10-03T15-42-00Z&p-_endTime=2023-10-04T15-42-00Z&p-_entityIds=v-tr21509.eastus2-a.worker.database.windows.net&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) 

If the above SQL change is not identified as the culprit, lets dig into node’s the SQL cluster is hosted on find host changes 

For the above SQL cluster, the node identified is: 668fd9f1-ceb8-6d43-606c-280cde4c930c ( SQL team can provide the node’s on which the Cluster is hosted) 

**Changes for Nodes:**

1. Go to [Node View](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_nodeid=all&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43) 
2. Get the nodes affected in the comma separated format, in this case : 668fd9f1-ceb8-6d43-606c-280cde4c930c  
3. Enter the above comma separated values into NodeId filter and set the time line correctly, recommended to use –24 hrs as the start time from the incident start time. There are scenarios where the issue was latent, so se the time filters as needed. 

<img src="media/nodeViewSQL.png" alt="alt text" width="1000"/>

Dashboard link : [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-10-03T15-42-00Z&p-_endTime=2023-10-04T15-42-00Z&p-_nodeid=v-668fd9f1-ceb8-6d43-606c-280cde4c930c&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43) 

**Identifying TOR, T1, T2 Changes for the Node:** 

The connection to the Node can be lost/interrupted due to update to the TOR, T1’s, T2’s connected to the Node. Since TOR is single point of failure, check for Tor updates. (There is more redundancy for T1 and T2, so mostly T1, T2 changes do not impact the Node). 

The node information table in node view provides a summary and details of the node, example cluster, TOR, number of changes made to TOR, T1, number of changes made to T1, is the node batched, node allocation type (Empty Node, MultipleUpdate) etc. 

To Identify ToR, T1 and T2 changes, go to Node View and select the nodeid, follow the same steps as identifying node changes mentioned above. 

After the filters are set and queried for changes, scroll down in the Node view to look for TOR, T1 and T2 changes 

<img src="media/t1t2t0SQL.png" alt="alt text" width="1000"/>

Dashboard Link: [here](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=2023-10-03T15-42-00Z&p-_endTime=2023-10-04T15-42-00Z&p-_nodeid=v-668fd9f1-ceb8-6d43-606c-280cde4c930c&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43)


