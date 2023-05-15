# Queries
<!--[Here is more information on Helper functions and Sample queries for broad searches](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/SitePages/FCMKustoWiki.aspx)-->

## View top 100 Changes 

### By Service Name

<span style="font-family:Courier New; color:orange;">ChangeEvent | where ServiceName == 'Federated Change Management' | top 100 by TIMESTAMP desc</span>

I know the service guid of a service / microservice in service tree and I want to pull the changes for that service.  Below functions enables this. The following example filters SLB changes for a given time range. ​

<span style="font-family:Courier New; color:orange;">GetChangesByService(@'889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f','1-12-2023 22:00:00','1-12-2023 23:00:00')</span>

### By Component Name

<span style="font-family:Courier New; color:orange;">ChangeEvent | where ComponentName == '<ComponentName>' | top 100 by TIMESTAMP desc </span>

*Note that TIMESTAMP or PreciseTimestamp most closely mirrors the approximate time the event was picked up by FCM. Note that ActualStart, ScheduledStart, etc. can be used instead if that is preferred.*

## View Location-Based Changes

### Changes By Location
I know the exact or partial location name. I want to pull changes for that location for a given time range. Use the below function which pull the changes for any locations.
Example below pulls changes for West US in the locationname.

<span style="font-family:Courier New; color:orange;">GetChangesByLocation(@'west us','1-12-2023 22:00:00','1-12-2023 23:00:00')</span> 

<!--need to see if this query works, receiving errors>

*Note: Column LocationName contains ClusterNames when LocationType = 'Cluster', this can then be joined with other data sources like AzureGraph. You don't have to use these columns unless necessary.*

<!--Here are the options to filter the data by Datacenter. Usually first 3 characters (or 5 characters) of the cluster name will represent DC code. Usually this should be sufficient to pull changes.
Still, given the clusteriIf you do not know the DC code,
1.     Get the 3 letter DC code from DCMT.
\\reddog\builds\branches\dcmt_latest_amd64\Datacenter
2.     Use the 3 /5 letter code in the query as the location. Location is a 'contains' query so 3 / 5 letter code is sufficient to pull changes.-->

### Changes By Location and Service
I know the Location and I want to filter further by using ServiceTree guid of the service / microservice. Below query filters the changes for "West US" and further filters for SLB service using the Service Tree ID.

<span style="font-family:Courier New; color:orange;">GetChangesByLocationAndService(@'west us','889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f','1-12-2023 22:00:00','1-12-2023 23:00:00') </span>

### Changes within a Time Range

I want to pull all changes for all services for a given timeline. Then use the below function.Note: Considering the amount of change data there is and Kusto limitation, we are restricting this query to work for only last 3 days of data.

<span style="font-family:Courier New; color:orange;">GetAllChangesForTimeRange(@'1-12-2023 22:00:00','1-12-2023 23:00:00')</span>