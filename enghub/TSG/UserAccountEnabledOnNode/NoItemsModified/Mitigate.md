# Mitigation steps for No Items being Modified Failure

1) Run the following query to double check whether there is data entering to FCM from the change source system or not:

```
let changeSourceSystem = '<Name of the changeSource System>';
cluster('fcmdataro.kusto.windows.net').database('FCMKustoStore').ChangeEvent 
 | where TIMESTAMP >= ago("enter the time span here Ex: 30m")
 | where ExternalSourceName contains changeSourceSystem
```

  > [!Note]
  Set the name of the changeSourceSystem based on the incident and the monitor that got triggered.

  > [!Note] 
  Set the Timespan based on the incident and the monitor that got triggered.

2) If there are any rows, that it's a false alarm, so you can mitigate the incident
3) If there are no rows, check for failures in QoS Logs in Jarvis:
https://jarvis-west.dc.ad.msft.net/4489B5DB
