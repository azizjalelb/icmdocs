## Change insight availability by Orchestrators

| Supported Deployment Systems | Change Data Onboarded | Change Data Granularity
| --- | --- | --- | --- | --- |
| PF (generic) | Yes [(Sample Data)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_entityType=v-pfenvironment&p-_entityType=v-pfenvironment%3Aagg&p-_entityType=v-pfmachine&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) * (PF Maintenance Service rebootful in progress) | PFCluster, Environment, MachineFunction, Machine |
| AzDeployer | Yes [(Sample Data)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=3hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_source=v-azdeployer&p-_entityType=all&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) | Zone, Custom |
| EV2 | Yes [(Sample Data)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=3hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_source=v-expressv2&p-_entityType=all&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) | Region |
| FUSE | Yes [(SampleData)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=3hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_source=v-fuse_fuse&p-_entityType=v-clusterspine&p-_entityType=v-dcspine&p-_entityType=v-node&p-_entityType=v-torrouter&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) | ToR, Device/Switch |
| XStore(DynamicConfigChangedEvent,WADI) | Yes [(Sample Data)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=3hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_source=v-xstore-wadi&p-_source=v-xstore-xds&p-_entityType=all&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) | Storage Stamp |
| DC Ops | Yes | DC, COLO, ROW, RACK |
| Asguard(WARP, AzCP, AsguardRCore, AsguardCore) | Yes | SF Tenant, UpdateDomain |
| Sql/CosmosDB Ring (SF) | Yes [(Sample data)](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=3hours&p-_endTime=now&p-_entityIds=all&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_source=all&p-_entityType=v-microsoft.sql.cluster&p-_payload=all&p-_serviceTreeIds=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) | Ring |
| GenevaActions | Yes | Region |
| AzCIS | Yes | Cluster |
| AzDM | Yes | AzDM Tenant |
| OAAS | Yes | node,container,cluster,tenant,soc..etc |

## Change data coverage by QCS, HVT,TCB
[ChangeInsights Coverage](https://aka.ms/fcmcoverage)