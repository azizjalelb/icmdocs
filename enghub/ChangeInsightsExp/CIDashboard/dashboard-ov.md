## **Dashboard Overview**

The **OneDeploy FCM Dashboard** is built on top of the Entity Model data. It provides several views that allow DRIs to find changes made during a specific time frame, at a given location, or by a particular service.

* **Zoom Levels** : DRIs can zoom out to see changes at a region level or zoom in to view changes at an entity level.
* **Service Deployment Progression (SDP)** : View the progression of deployments for a given payload.

### **When to Use Each of the Views**

1. **Host Changes** :

* **Access** : [Host Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_region=all&p-_cluster=all&p-_serviceName=all&p-_payload=all#91d01f68-e694-4da7-9181-641151bec452)
* **Description** : Provides a summary of host updates made to a selected region or cluster for a given time range.

1. **Host Drill-Down View** :

* **Access** : [Host Drill Down View](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=24hours&p-_endTime=now&p-_nodeid=v-b2931fbe-fa10-ac0e-405b-661dd86838f6%2Cdd7577c4-aa26-bc96-a722-9b3853823d2d%2C2c1020f8-8b86-eb66-37b7-73246329ed14%2C9f4eadd2-0ec0-f8cb-25da-5e698058d0de&p-_dynamicMeasure=all&p-_entityTypeNode=all#08c31477-dfa3-43d3-9427-a6a57b228c43)
* **Description** : Shows changes made to selected nodes with timelines of regressed measures, node information, and changes to ToRs, Cluster Spines, and DC Spines.

1. **Customer View** :

* **Access** : [Customer View](https://dataexplorer.azure.com/dashboards/40fa7846-b756-40a6-a0e4-a77e5bc09767?p-_customer=v-Walmart+Inc.&p-_startTime=1hours&p-_endTime=now&p-_nodeid=all&p-_region=all&p-_veName=all&p-_payload=all&p-_impactful=v-All&p-_noflyzone=all#f4aa9e20-a815-486c-a1c3-1a5a279e64eb)
* **Description** : Provides a summary view of host updates made to customer VMs, including batched updates, scheduled events, OM rollouts, and live migrations.

1. **Subscription/VM View** :

* **Access** : [Subscription/VM View](https://dataexplorer.azure.com/dashboards/40fa7846-b756-40a6-a0e4-a77e5bc09767?p-_startTime=1hours&p-_endTime=now&p-_dynamicMeasure=all&p-_entityTypeNode=all&p-_subscriptionId=all#25eab919-a8e8-4c35-abdc-4d572d872d1f)
* **Description** : Shows changes to all nodes hosting the VMs under a specific subscription or ARM resource.

1. **Payload Details** :

* **Access** : [Payload Details](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_source=all&p-_entityType=all&p-_payload=v-20231026-185824-af6b08181292abb827cab2975b699c51bc186aae#84c6c83e-687d-44a3-a599-110f700efce7)
* **Description** : Provides risk scores, payload owners, node counts, SDP details, and bypasses for a given payload.

1. **All Changes** :

* **Access** : [All Changes](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=24hours&p-_endTime=now&p-_entityIds=all&p-_region=v-apac+southeast+2&p-_region=v-austria+east&p-_region=v-east+us+2&p-_availabilityZone=all&p-_datacenter=all&p-_cluster=all&p-_serviceName=all&p-_icmTeamName=all&p-_source=all&p-_entityType=all&p-_veName=all&p-_payload=all&p-_payloadOwner=all#66cc3653-ecde-4c2c-9d24-1838d351d4d4)
* **Description** : Use this view to see detailed information about changes—where, when, who, and what.

---

## **4. Frequently Asked Questions (FAQs)**

1. **What changes are happening in an impacted region?**

   * **Answer** : Navigate to the [Top-Level View](InterfaceHowTo/TopLevelView.md) to view all changes made in a region or by a service.
2. **Are there any payloads of high risk being deployed?**

   * **Answer** : Go to the [Change Details View](InterfaceHowTo/ChangeDetails.md) and sort by risk score to identify high-risk payloads.
3. **Are there any host updates being deployed?**

   * **Answer** : Use the [Change Details View](InterfaceHowTo/ChangeDetails.md) and filter for host updates within your time range and region.
4. **Are there any control plane changes?**

   * **Answer** : In the [Change Details View](InterfaceHowTo/ChangeDetails.md), focus on control plane services to find recent changes.
5. **Are there any host networking changes?**

   * **Answer** : Filter by the "Host Networking" service in the [Change Details View](InterfaceHowTo/ChangeDetails.md) to find relevant changes.
6. **Is there an example for navigating control plane changes?**

   * **Answer** : Review the example in the [Example Scenarios](Scenarios.md) section.
7. **Is there a video that I can watch?**

   * **Answer** : Yes, a training video is available for further guidance.

   <iframe src="https://microsoft.sharepoint.com/teams/FCM/_layouts/15/embed.aspx?UniqueId=4f607e9e-e6b8-45cf-8ad5-3aa3e1ee1e2b&embed=%7B%22hvm%22%3Atrue%2C%22ust%22%3Atrue%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="640" height="360" frameborder="0" scrolling="no" allowfullscreen title="Training Video"></iframe>

Examples and Scenarios
======================

We have organized the Examples and Scenarios into separate subpages for easier navigation and readability. Please refer to the following scenarios:

- A. End-to-End Scenario: Subscription/VM - CRI from Tesco Reporting Unexpected Impact
- B. End-to-End Scenario: Host Changes - Payload Details, Host Drill Down
- C. End-to-End Scenario: Customer View - Payload Details, Host Drill Down

Additionally, we have provided guidance on navigating incidents involving specific types of changes:

- Navigating Incidents That Involve Control Plane Changes
- Navigating Incidents That Involve Networking Changes
- Investigating Unhealthy SQL Tenants and Host-Related Culprits
