# Mitigation steps for MDS EventProcessor Failures
1) Login to Azure Portal with AME credentials.

2) Find the Application Insights "MDSEventProcessor" and run the following query in the logs tab:

```
customMetrics|where timestamp >ago(1d)| where name=="ProcessMDSEventsFunction Failures" and value>0 |project cloud_RoleName,appId,timestamp,cloud_RoleInstance
|join kind= inner(exceptions|where timestamp >ago(1d)) on $left.cloud_RoleInstance==$right.cloud_RoleInstance  
| where outerMessage!contains("bloblease") and outerMessage!contains("LeaseLost") and  outerMessage!contains("New receiver 'nil' with ") 
| project timestamp,cloud_RoleName,outerMessage,innermostMessage 
| order by timestamp  desc
```

 > [!Note]
 Adjust the time accordingly.
 
 3) If the issue is related to getting a certificate from a keyvault, reach out to AKV team and look for help from them.

 4) If the issue is related to Redis Cache, investigate and evaluate whether to increase the capacity of Redis Cache.
