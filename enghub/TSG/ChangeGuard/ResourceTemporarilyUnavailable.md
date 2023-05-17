# ChangeGuard - Resource temporarily unavailable

## Overview

> [!NOTE] Possible same resolve as this similar [ICM Incident](https://portal.microsofticm.com/imp/v3/incidents/details/388871407/home).

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is a Canary, which makes calls to all the other services at regular intervals, checking the health
of each one.
During deployments (either scheduled Change Guard deployments or fleet level deployments to AKS or the nodes hosting the
cluster) there is a possibility that the connection to the service/AKS pod might drop and trigger an alarm.

### Steps taken to investigate the issue:

#### 1. Search for the alert that was fired.

In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the
alert that was fired.

#### 2. Check the description of the incident for the stack trace and verify if it was indeed triggered by the Canaries, for example:

```
"{\"FunctionName\":\"HttpGetWithClientCertAsync\",\"Status\":\"SystemError\",\"DurationMilliSec\":\"48.3402\",
\"Type\":\"Critical\",\"HttpStatus\":\"0\",\"Class\":\"Utils\",\"System\":\"Canaries\",\"TimeStamp\":\"2023-03-08T15:02:29.3992255Z\",
\"Message\":\"Connection refused (changeguard.fcm.azure.microsoft.com:443)\",
\"FunctionArguments\":\"host:'https://changeguard.fcm.azure.microsoft.com', path: '/api/eventsretrieval/events/', 
query: '?&startDate=2021-01-01T00:00:00Z&endDate=2031-12-31T23:59:59Z' certLocation: '/app/certs/chggrd-client-cer-prod.pfx',
 correlationId: '789ed3bf-f92d-44d1-9b6c-d79d77f4068e'\",\"ErrorMessages\":\"HResult: -2147467259: 
 Connection refused (changeguard.fcm.azure.microsoft.com:443)\\
 ```

In the previous example the error relates to Canaries.HttpGetWithClientCertAsync.

#### 3. Go to query results inside App Insights and investigate the logs.

```
traces
| where severityLevel >= 4
| where message contains "Resource temporarily unavailable"
```

What is meaningful is to see `who` triggered the alarm (e.g.: the Canaries services, method
HttpGetWithClientCertAsync/HttpPostWithClientCertAsync), how many `occurrences` the alarm had and the `time interval` it
fired.

#### 4. By checking the number of occurrences and the time interval we can deduct if it was a transient error due to a deployment (either App deployment or fleet deployment) and if there were any other issues since then.

If the the number of occurrences is small and it fired only inside a small window (in the range of several seconds) the
issue could be considered transient.

#### 5. Test the cluster and the Change Guard services to see if everything is working as expected.

The documentation on how to test each part of the system can be found in
the [README.md](https://msazure.visualstudio.com/One/_git/FCM-ChangeManager?path=/src/README.md) file inside the repo.

#### 6. If the testing concludes with everything working, and no alert fired after the initial time window, the incident can be marked as resolved.

> [!NOTE]
> - If the alert is triggered by Canaries, during a deployment, and the occurence count is 1-2, then the incident can be
    auto-resolved.
> - If the alert is triggered by another service, please contact the SME in charge of this system for further details.