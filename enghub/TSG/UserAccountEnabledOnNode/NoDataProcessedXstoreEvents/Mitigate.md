# Mitigation steps for  No Data being processed from Xstore Events Failure

1) Run the following query to double check whether there is data entering to FCM from the change source system or not:

```
cluster('fcmdataro.kusto.windows.net').database('FCMKustoStore').ChangeEvent 
 | where TIMESTAMP >= ago("enter the time span here Ex: 30m")
 | where ExternalSourceName contains 'xstore'
```

  > [!Note] 
  Set the Timespan based on the incident and the monitor that got triggered.

2) If there are any rows, that it's a false alarm, so you can mitigate the incident
3) If there are no rows, check for failures in QoS Logs in Jarvis:
https://jarvis-west.dc.ad.msft.net/4489B5DB

4) Login to Azure Portal with your AME Credentials.

5) Go to Function App, find "xstoreeventprocessoreast", click on it, and go to Application Insights for this function app from the panel on the left. The Application Insights is called "mdseventprocessorlogs".

6) Look for exceptions for Xstore by running the query below in the "Logs" tab:

    ```
    exceptions 
    | where problemId contains("xstore") 
    | order by timestamp desc
    ```

![xstoreFailureMitigation](../Images/xstoreFailureMitigation.png)

7) Take necessary action as per the error messages. 
