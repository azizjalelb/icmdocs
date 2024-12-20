<h1>OneDeployFCM Dashboard (aka.ms/onedeployfcm)</h1>

<h2>Dashboard Overview: </h2>
The One deploy fcm dashboard has been built on top of the Entity Model data. The dashboard provides several views that allows the DRIs to find changes that were made at a given time duration, and/or, at a given location, and/or, by a given service. It allows the DRIs to zoom out for changes at a region level, or zoom in for changes at a given entity level, and everything in between.  DRIs can also see the SDP progression for a given payload.

If you need access please add your-self to the idweb group: [fcmusers](https://idweb.microsoft.com/IdentityManagement/aspx/common/GlobalSearchResult.aspx?searchtype=e0c132db-08d8-4258-8bce-561687a8a51e&content=fcmusers).

<h2>When to use each of the views?</h2>

[Host Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_region=all&p-_cluster=all&p-_serviceName=all&p-_payload=all#91d01f68-e694-4da7-9181-641151bec452) provides a summary of host updates made to a selected Region or Cluster for a given time range.

[Host Drill Down View](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=24hours&p-_endTime=now&p-_nodeid=v-b2931fbe-fa10-ac0e-405b-661dd86838f6%2Cdd7577c4-aa26-bc96-a722-9b3853823d2d%2C2c1020f8-8b86-eb66-37b7-73246329ed14%2C9f4eadd2-0ec0-f8cb-25da-5e698058d0de&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43) – provides changes made to the selected node(s) with timeline of the regressed measures. Contains node information (is the node batched, allocation type) and changes made to the Tor’s (T0), ClusterSpine(T1), DCSpine(T2).

[Customer View](https://dataexplorer.azure.com/dashboards/40fa7846-b756-40a6-a0e4-a77e5bc09767?p-_customer=v-Walmart+Inc.&p-_startTime=1hours&p-_endTime=now&p-_nodeid=all&p-_region=all&p-_veName=all&p-_payload=all&p-_impactful=v-All&p-_noflyzone=all#f4aa9e20-a815-486c-a1c3-1a5a279e64eb) – provides a summary view of host updates made to customer VM(s) such as Batched updates, Scheduled Events, OM rollouts, Live Migration etc.

[Subscription/VM View](https://dataexplorer.azure.com/dashboards/40fa7846-b756-40a6-a0e4-a77e5bc09767?p-_startTime=1hours&p-_endTime=now&p-_dynamicMeasure=all&p-_entityTypeNode=all&p-_subscriptionId=all#25eab919-a8e8-4c35-abdc-4d572d872d1f) – provides a subscription or ARM Resource (VMSS/VM) level view to show changes to all the nodes the VM(s) are hosted on. 

[Payload Details](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_source=all&p-_entityType=all&p-_payload=v-20231026-185824-af6b08181292abb827cab2975b699c51bc186aae#84c6c83e-687d-44a3-a599-110f700efce7) – provides the risk score of the payload, payload owner, total count of nodes that have received the payload, SDP details and SDP bypasses.

[All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=24hours&p-_endTime=now&p-_entityIds=all&p-_region=v-apac+southeast+2&p-_region=v-austria+east&p-_region=v-east+us+2&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4)– Use this view to see the details of the changes – Where was the change applied ? When was the change applied ? By who was the change applied? What was the change ? Expected Impact of the change? Navigate to the Payload View and Host Drill Down View from here to get specific details of the payload or node.  Navigate to the health dashboards as well from here to get specific details of what metrics contributed to the risk scores. 


<h2>FAQs</h2>

1. What changes are happening in an impacted region?  
    - Navigate to the [Top Level Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=12hours&p-_endTime=now&p-_region=all&p-_cluster=all&p-_serviceName=v-Host+Networking&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#a2b4dbc9-e958-4054-bc3e-6677c4321dd9) tab to view all the changes made in a region or all the changes made by a service 

    - Follow the steps [here](InterfaceHowTo/TopLevelView.md#toplevelView) to find the changes that have been made in a region. 

2. Are there any payloads of high risk being deployed? 

    - Navigate to the [All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=6hours&p-_endTime=now&p-_entityIds=v-uswestcentral-prod-a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) tab and follow the steps [here](InterfaceHowTo/ChangeDetails.md#payloadRisk). 

    - Knowing the payloads with highest risk will help to engage the right service team DRI 

3. Are there any host updates being deployed? 

    - This is often asked during incident investigation. 

    - Navigate to the [All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=6hours&p-_endTime=now&p-_entityIds=v-uswestcentral-prod-a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) tab and follow the steps [here](InterfaceHowTo/ChangeDetails.md#hostUpdate). 

4. Are there any control plane changes?  

    - Navigate to the [All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=6hours&p-_endTime=now&p-_entityIds=v-uswestcentral-prod-a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) tab to view details of changes made 

    - Follow the steps [here](Scenarios.md#controlPlaneChanges) to find control plane changes 

5. Are there any host networking changes?  

    - Navigate to the [All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=6hours&p-_endTime=now&p-_entityIds=v-uswestcentral-prod-a&p-_region=all&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=v-Azure+Cosmos+DB&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4) tab to view details of changes made 

    - Follow the steps [here](InterfaceHowTo/ChangeDetails.md#hostUpdateNetworking) to find changes made by “Host Networking” Service 

6. Is there an example for navigating control plane changes? 

    - Review the example [here](Scenarios.md#navigatingControlPlaneChanges) 

7. Is there an example for navigating an incident involving Networking changes? 

    - Review the example [here](Scenarios.md#networkingChanges) 

8. Is there an example for navigating an incident involving Storage changes? 

    - Review the example [here](Scenarios.md#storageChanges)

9. Is there a video that I can watch? 

<iframe src="https://microsoft.sharepoint.com/teams/FCM/_layouts/15/embed.aspx?UniqueId=4f607e9e-e6b8-45cf-8ad5-3aa3e1ee1e2b&embed=%7B%22hvm%22%3Atrue%2C%22ust%22%3Atrue%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="640" height="360" frameborder="0" scrolling="no" allowfullscreen title="Meeting-20231117_192800-Meeting Recording.mp4"></iframe>
