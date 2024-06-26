# ChangeInsights in ICM User Guide

## Overview
 ChangeInsights provides relevant changes for all Azure (Sev0,1,2) incidents, which enables DRI's to see changes potentialy causing the incident.
 To provide relevant changes for an incident, the three important dimensions needed are
1. When (Time range for change search, we search for time range of last 12 hrs from the impact start time).
2. Where ( The granular location where the impact is happening, the granular the location like "node", "torrouter","cluster"..etc , the changes will be relevant
           For services operating at region, the impact region in ICM should be specified).
3. Who (The service responsible for the incident).

| ICM location | Search Criteria | Results | Notes
|:-----|:-----|:-----|:-----|
| Region | Region+Service|Show top 10 change made by Sevice in the Impacted region for last 12hrs| Changes to any EntityType by that Service in that Region|
| Cluster | Cluster|Show top 10 change made to the Cluster for last 12hrs| Changes made to Cluster, Nodes, ToR|
| Node | Node|Show top 10 change mades to the Node for last 12hrs| Changes made to the Node,ToR|
| ToR | ToR|Show top 10 change mades to the ToR for last 12hrs| Changes made to the ToR|

The following are the currently supported deployment Systems


| Supported Deployment Systems
|:-----|
|PF|
|AzDeployer|
|EV2|
|FUSE|
|WADI(Xstore)|

## Identifying "Where"(impacted location) in ICM

Change Insights uses location (Where) in the incident to provide relevant changes in the incident

1. Impacted Regions 
   ![alt text](media/ImpactedRegions.png)
2. Detected DC/Region
  ![alt text](media/DetectedRegionDC.png)
3. Instance/Cluster 
  ![alt text](media/InstanceCluster.png)
 
## How to map "Where"(impacted location) in ICM
### Service using EV2 (Above ARM services) for deployments

#### Monitor Raised incidents -Detected DC/Region

  To identify the impacted region for the incident, ChangeInsights relies on Impacted Regions in ICM


##### How to map MDM dimension to ICM DC/Region

 ![alt text](media/Monitor-RegionMapping.png)
  
#### Manually Raised incidents - Impact Region
  To identify the impacted region for the incident, ChangeInsights relies on Impacted Regions in ICM



### Service using AzDeployer/PF (Below ARM services) for deployments

Provide granular location (Cluster, node) to identify relevant changes.

#### Monitor Raised incidents - specify impacted cluster

  To identify the impacted cluster for the incident, ChangeInsights relies on  "Instance/Cluster" field in ICM

  ![alt text](media/InstanceCluster.png)

##### How to map MDM dimension to "Instance/Cluster" field in ICM

 ![alt text](media/Monitor-InstanceClusterMapping.png)

 #### Incidents - specify impacted Nddes for an incident

  To identify the impacted node for the incident, ChangeInsights relies on  "Instance/Cluster" field in ICM

  ![alt text](media/InstanceCluster-Node.png)
  
#### Manually Raised incidents - Instance/Cluster

  To identify the impacted cluster/node for the incident, update "Instance/Cluster" field in ICM

  ![alt text](media/InstanceCluster.png)




<!-- ### User Interface 
Check out our demo video here!
-->

