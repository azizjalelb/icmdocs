# ChangeGuard - Arcus SDK High Latency

## Overview

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is Change Assessment, which is used to load BoQ data from Safefly.

One of the reasons the Change Assessment might fail is due to latency issues.

### Steps taken to investigate the issue:

#### 1. Search for the alert that was fired.
In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the alert that was fired.

#### 2. Go to query results and investigate the logs.
Query: 
```
traces
| where severityLevel >= 4
| where message has "Arcus SDK High Latency" 
```
In this case the logs mentioned that Change Guard can not call the Arcus Sdk service due to a time out error:
```
"Arcus SDK High Latency".
```

#### 3. Check that Aks Cluster resources are not overloaded
Go to 'chggrd-api-aks-prod' Kubernetes service and navigate to 'monitoring' tab.
Check the metrics graphs and notice if any resource is over 90%.
If this is the case,  further investigation is needed to see which services/pods occupy the most resources, and dig down to see which calls take the longest.
In case restart of the pods in the cluster is needed, this can be done *either* by:
- Stopping and starting the AKS cluster (*THIS WILL TRIGGER DOWNTIME* of the whole cluster)
- *OR*
- Restarting each service deployment using the command `kubectl rollout restart deployment deployments/[DEPLOYMENT_NAME] -n [NAMESPACE]`. This command needs to be repeated for each impacted deployment/service. For PROD: kubectl rollout restart deployment deployments/changeassessment-deployment -n changeguard-ns

Test everything to see if the problem is resolved.
Steps:
- Check if the alert is still firing.
- Check the app insights logs to see if failures are still appearing.
- Test using the portal.
- Test using Postman calls to the cluster/services.

#### 4. Get in contact with Arcus Sdk team to see if there is any deployment/update/fix going on at their end(mamegh@microsoft.com)