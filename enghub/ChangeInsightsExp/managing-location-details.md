**5\. Managing Location Details in Change Insights**
----------------------------------------------------

Accurate location data is essential for the **Change Insights** platform to deliver relevant and actionable information during incidents. The granularity and accuracy of the location data determine which changes are presented to the Designated Responsible Individuals (DRIs), helping them isolate potential root causes of an incident more effectively.

This section will guide you on how to manage, edit, and utilize location details within **ICM** and **Change Insights**. Understanding and keeping location data accurate can significantly improve the precision of change investigations and reduce incident resolution time.

---

### **5.1 Importance of Accurate Location Data**

Location data plays a pivotal role in determining which changes are relevant to an incident. The more specific and granular the location details, the more targeted and accurate the change data provided by Change Insights. Here's why location data is critical:

1. **Narrowing Down Changes**: Change Insights uses location data to filter out irrelevant changes and focus only on those that could have impacted the specific location of the incident. Without accurate location data, DRIs may be flooded with unnecessary or unrelated changes.
2. **Granular Impact Analysis**: Precise location data helps Change Insights analyze changes at different levels of granularity, such as **region**, **cluster**, **node**, or even a **ToR (Top-of-Rack switch**). This allows DRIs to zoom in on potential problem areas quickly and efficiently.
3. **Real-Time Updates**: When incident location data is updated, Change Insights refreshes its results to ensure that DRIs are always working with the most relevant changes. This helps prevent investigating outdated or irrelevant changes.

#### **Examples of Location Data Use Cases**:

- **Region-Level Impact**: For incidents affecting an entire Azure region (e.g., `East US 2`), location data helps Change Insights identify changes made at the region level, such as network configuration updates or service deployments.
- **Node-Level Impact**: For more localized incidents, such as those affecting specific nodes in a data center, accurate node IDs ensure that only changes relevant to those nodes are presented, speeding up root cause analysis.
- **Cluster-Level Impact**: For cluster-wide issues, accurate cluster data allows DRIs to track changes affecting the specific cluster in question, without being distracted by irrelevant changes in other clusters or regions.


### **5.2 Prerequisites for Surfacing Change Insights**

To provide relevant changes for an incident, three important dimensions are needed:

1. **When** : The time range for change search. Typically, Change Insights searches for changes within the last **12 hours** from the incident's impact start time.
2. **Where** : The granular location where the impact is happening. The more specific the location (e.g., node, ToR, cluster), the more relevant the changes will be.
3. **Who** : The service responsible for the incident. Specifying the affected service helps filter changes made by that service.


### **5.3 Editing Location Details in ICM**

During an incident, it's important that DRIs keep the location data updated in the ICM portal. Accurate and up-to-date location information allows Change Insights to provide more relevant data and improve incident resolution speed.

Change Insights also supports various location/entity types to provide insights for an incident. The locations must match standard locations specified in the source data.

#### **Table: Supported Location Types and ICM Fields**


| **ICM Location**      | **Source**       | **Search Criteria** | **ICM Field Required**                              | **Results**                                                                           | **Notes**                                                |
| ----------------------- | ------------------ | --------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Region**            | [FCM Regions]()  | Region + Service    | Impacted Region(s)                                  | Shows top 10 changes made by the service in the impacted region for the last 12 hours | Changes to any EntityType by that service in that region |
| **Cluster**           | [FCM Clusters]() | Cluster             | Instance/Cluster (comma-separated list)             | Shows top 10 changes made to the cluster for the last 12 hours                        | Changes made to Cluster, Nodes, ToR                      |
| **Node**              | [FCM Nodes]()    | Node                | Instance/Cluster (comma-separated list of node IDs) | Shows top 10 changes made to the node for the last 12 hours                           | Changes made to the Node, ToR                            |
| **ToR (Top-of-Rack)** | [FCM ToRs]()     | ToR                 | Instance/Cluster (comma-separated list of ToR IDs)  | Shows top 10 changes made to the ToR for the last 12 hours                            | Changes made to the ToR                                  |

*Note: Change Insights picks up the most granular location provided in the above fields while providing insights for an incident.

#### **Steps to Edit Location Details**:

1. **Navigate to the Incident**:

   - Go to the [ICM Portal](https://icm.microsoft.com/) and open the incident you are managing.Go to the ICM portal and open the incident you are managing
2. **Locate the Impacted Regions/Entities Section**:

   - On the incident details page, find the **Impacted Regions** or **Entities** section. This will typically show the current location details that are being used by Change Insights.
3. **Edit Location Fields**:

   - If the current location details are incorrect or incomplete, you can edit them by clicking the **Edit** button next to the location fields.
   - **Fields to Edit**:
     - **Region**: Specify the affected Azure region (e.g., `East US 2`).
     - **Cluster**: If applicable, specify the affected cluster (e.g., `Cluster: hkg21prdstf01`).
     - **Node**: For node-specific incidents, enter the affected node IDs.
     - **ToR** : If applicable, enter the affected ToR IDs.
4. **Save the Changes**:

   - After editing the necessary fields, click **Save** to update the location data. Once saved, Change Insights will refresh its data to reflect the new location information.
5. **Monitor Changes**:

   - After updating the location details, monitor the **Troubleshooting Tab** and **AI Summary** for refreshed change data based on the new location. This helps ensure that you are working with the most relevant and up-to-date information.

#### **When to Update Location Details**:

- **Initial Incident Setup**: Always ensure that the correct location data is entered when the incident is first created.
- **Incident Escalation**: If the impact area grows or shifts (e.g., from a node-level impact to a region-level issue), update the location details immediately to adjust the scope of changes presented by Change Insights.
- **Post-Incident Review**: After resolving an incident, reviewing location data accuracy can help improve future incident responses by ensuring that location information is consistently accurate.

---

### **5.3 Impact of Location Data on Change Insights**

The accuracy of location data directly impacts the relevance of the changes presented in Change Insights. Here are some ways that accurate location data can improve your use of the platform:

#### **1\. Better Filtering of Changes**:

- **Granular Filters**: By providing more specific location data, such as node IDs or cluster information, Change Insights can filter out irrelevant changes and surface only those affecting the exact location of the incident.
- **Example**: For a node-specific incident, if the node IDs are correctly entered, Change Insights will prioritize changes made to those nodes rather than displaying region-wide changes that may not be relevant.

#### **2\. Real-Time Updates**:

- **Location Refreshes**: When location data is updated, Change Insights automatically refreshes the list of changes based on the new information. This helps DRIs focus on the most relevant data as the incident evolves.
- **Example**: If an incident initially affects a single node but later spreads to a whole region, updating the location to the region level will immediately surface region-wide changes that could be contributing to the expanded impact.

#### **3\. Accurate Health Correlation**:

- **Health Anomalies**: By aligning location data with health anomalies detected in specific regions, clusters, or nodes, DRIs can better correlate changes to the incident's symptoms. This helps isolate the root cause more quickly.
- **Example**: If a health anomaly is detected at the cluster level, but the location data only specifies a region, updating the location to the cluster level allows Change Insights to filter out region-wide changes and focus on changes made to the cluster.

---

### **Best Practices for Managing Location Data**

To ensure that Change Insights provides the most accurate and relevant data, follow these best practices when managing location details:

1. **Be as Specific as Possible**:

   - Always use the most specific location data available, whether it's a node ID, cluster name, or region. This helps Change Insights deliver more targeted change information.
2. **Update Locations in Real-Time**:

   - As the impact area of an incident evolves, update the location data immediately to ensure that Change Insights keeps providing relevant changes. This can save valuable time during incident resolution.
3. **Cross-Check Location Data with Service Teams**:

   - When managing incidents involving multiple teams or services, cross-check location data with the teams responsible for the impacted areas. This helps ensure that all relevant changes are surfaced.
4. **Review Post-Incident**:

   - After an incident is resolved, review the accuracy of location data to improve future incident responses. Document any discrepancies or improvements needed in the incident's retrospective.

---

By understanding how to manage and edit location details in ICM, you can enhance the precision and relevance of the changes surfaced by **Change Insights**. Accurate location data not only improves the efficiency of incident resolution but also helps reduce unnecessary investigation into irrelevant changes, saving time and resources for your team.
