FCM in [Kusto​](https://aka.ms/kusto) enables engineers to answer ad hoc questions about their changes in ChangeInsights. The data is queryable via the Service GUIDs (from ServiceTree) for their Service.

## Access

The FCM Change events are in the fcmdata kusto cluster, under the EntityModel database in table EntityChangeEvents.



To view this data through the Kusto Explorer, please go to: [fcmdata.EntityModel | Azure Data Explorer](https://dataexplorer.azure.com/clusters/fcmdata/databases/EntityModel) and run the below query


Execute [[Web](https://dataexplorer.azure.com/clusters/fcmdata/databases/EntityModel?query=H4sIAAAAAAAAA3PNK8ksqXTOSMxLT3UtS80rKeaqUShJzE5VMDQAANXLbsQcAAAA)][[Desktop](https://dataexplorer.azure.com/clusters/fcmdata/databases/EntityModel?query=H4sIAAAAAAAAA3PNK8ksqXTOSMxLT3UtS80rKeaqUShJzE5VMDQAANXLbsQcAAAA&web=0)]
```
cluster('fcmdata.kusto.windows.net').database('EntityModel').EntityChangeEvents
| take 10
```

### Permissions

Request access to the FCMUsers Security Group on http://idweb

### Supported Use

The dataset is intended for exploration and answering ad hoc questions.

- Reporting should be done against the Kusto datastream​​ from the follower https://fcmdataro.kusto.windows.net:443/EntityModel
- Service integration should be against the FCM APIs per agreed upon SLAs
- If you are seeing any of the Kusto limit errors while using 'Explore in lens' feature, please reduce the time window for which you are looking for data. Learn more here about [Query Limits](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/concepts/querylimits)