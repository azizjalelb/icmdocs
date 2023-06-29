
# Mitigation steps for ChangeManagerUI Failures
1)  Login to Azure Portal with your AME Credentials.

2) Go to "changemanagerui" Application Insights which is under "FCM Production" subscrtiption

3) Go to "Logs" tab from the panel on the left and run the query below:

```
    customMetrics 
    | where timestamp >= ago(1d)
    | join kind=inner (exceptions | where timestamp >= ago(1d)) 
    on $left.cloud_RoleInstance==$right.cloud_RoleInstance
    | order by timestamp  desc
```

4) Take action based on the error message.