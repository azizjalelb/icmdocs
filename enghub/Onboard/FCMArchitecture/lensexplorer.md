## Explore In Lens
Explore In Lens is a new feature in FCM, where you can explore the FCM data in Kusto via Lens dashboards. Explore In Lens feature provides an easier way for FCM users to have the filtered / selected data exploration in Len dashboard.

FCM data in Kusto is opened to partners for exploration. Teams can use this to join the change data with other data sources to produce better view of changes.

### Here are some details you would want to know:

- Changes in Kusto are recorded as Events when the change comes through FCM. The events are then deduped for easy consumptions and following functions are available for easy use or as a sample.
![alt text]

- If you are not able to see data due to access issues, then join "FCMUsers" group. Wait until you get approval and then you should be able to use this feature.

- Sometimes the data you see in FCM UI might be slightly different than what the Kusto query returns which is acceptable. This could be because:

    1. FCM UI has ways to group changes based on a parent record representing a Release / a higher level Roll out. Kusto queries doesn’t enable this out of box.

    2. The time range picked in both systems might be different or slightly off by few seconds between Kusto and FCM UI.

    3. There is a constant change data flow in both the systems. Although both the systems should be in sync in NRT, there might be a slight chance where one system might be latent by few min than the other.

    4. 'Physical Network' teams data in FCM has some data quality issues which are being tracked in this incident. This is causing some data different between FCM and Kusto.

- If you are seeing any of the Kusto limit errors while using 'Explore in lens' feature, please reduce the time window for which you are looking for data. Learn more here about [Query Limits](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/concepts/querylimits)

<!--- Data from some of the sources show deployments started long ago but they appear to be still open. The records still showing up in FCM-->

## Visualization in Lens
In​ addition through the use of Lens V2, one can create visualizations and dashboards to organize the change event data in whatever way they see fit. Lens V2 uses Kusto for their query language, making the transition to/from Kusto Explorer and Lens V2 relatively painless.

<!--- NOTE: UPDATE LENS DASHBOARD EXAMPLE

​To use a sample dashboard please go [here](https://lens.msftcloudes.com/v2/#/dashboard/View%20Most%20Recent%20Change%20Events?_g=(ws:ws-fcm-change-events)) --> 

​​Visit the [Lens wiki](https://eng.ms/docs/products/genevaanalytics/lensexplorer/lensuserguide​) for questions/guides about using Lens V2