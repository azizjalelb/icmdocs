# ChangeGuard - Arcus Sdk Latency Check

## Overview

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is Change Assessment, which is used to load BoQ data from Safefly.

One of the reasons the Change Assessment might fail is due to latency issues.

### Steps taken to investigate the issue:s

#### 1. Search for the alert that was fired.
In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the alert that was fired.

#### 2. Check that Aks Cluster resources are not overloaded
Go to 'chggrd-api-aks-prod' Kubernetes service and navigate to 'monitoring' tab.
Check the metrics graphs and notice if any resource is over 90%.
If this is the case, restart the pods in the cluster.
This can be done *either* by:
- Stopping and starting the AKS cluster (*THIS WILL TRIGGER DOWNTIME* of the whole cluster)
- *OR*
- Restarting each service deployment using the command `kubectl rollout restart deployment my-deployment`. This command needs to be repeated for each impacted deployment/service.

Test everything to see if the problem is resolved.
Steps:
- Check if the alert is still firing.
- Check the app insights logs to see if failures are still appearing.
- Test using the portal.
- Test using Postman calls to the cluster/services.

#### 3. Get in contact with Arcus Sdk team to see if there is any deployment/update/fix going on at their end(mamegh@microsoft.com)