# Sev2:Fired Application Insights Log [SEV-2] ChangeGuard Critical Event requires attention !!

## Overview

Same resolve as this similar [ICM Incident](https://portal.microsofticm.com/imp/v3/incidents/details/373402089/home).

The Change Guard APIs are deployed as services inside an AKS cluster. 
One of the services is a Canary, which makes calls to all the other services at regular intervals, checking the health of each one.
During deployments there is a possibility that the connection to the service/AKS pod might drop and trigger an alarm.

Check the description of the incident for the stack trace and verify if it was indeed triggered by the Canaries, for example: 
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

> [!NOTE]
> - If the alert is triggered by Canaries, during a deployment, and the occurence count is 1-2, then the incident can be auto-resolved.
> - If the alert is triggered by another service, please contact the SME in charge of this system for further details.