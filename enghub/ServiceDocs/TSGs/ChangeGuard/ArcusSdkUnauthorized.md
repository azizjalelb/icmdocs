# ChangeGuard - Arcus Sdk Authentication Failure

## Overview
> [!NOTE] Possible same resolve as this similar [ICM Incident](https://portal.microsofticm.com/imp/v3/incidents/details/387791153/home).

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is Change Assessment, which is used to load BoQ data from Safefly.

One of the reasons the Change Assessment might fail is due to invalid or expired certificates.

> [!NOTE]
> - The TSG for the Emergency Certificate Rotation, with all the details can be found [here](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/ChangeGuard/_layouts/15/Doc.aspx?sourcedoc={b1511488-1e3b-45b8-b1f3-b0b89a26b27a}&action=view&wd=target%28Emergency%20Certificates%20Rotation%20%28ECR%5C%29%20Drill.one%7C970fb975-853c-4b2f-9a7f-12c62a1b988d%2FChange%20Guard%20-%20PROD%20-%20Certificate%20Rotation%20Guide%7C862f4999-13c1-4904-af6a-821e5a8d61d7%2F%29&wdorigin=703).

### Steps taken to investigate the issue:s

#### 1. Search for the alert that was fired.
In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the alert that was fired.
#### 2. Go to query results and investigate the logs.
In this case the logs mentioned that Change Guard can not call the Arcus Sdk service due to an unauthorized error:
```
"PLACEHOLDER_EXCEPTION_MESSAGE".
```
Additional information:
```

```
#### 3. This led to check if the `Client` certificate used by the Change Assessment service, `chggrd-client-cer-prod`, is valid and has not expired.
The certificate can be found inside the KeyVault: `chggrd-client-cer-prod`.

If the certificate is expired, it has to be renewed.

In this case the latest version of the certificate was not expired.
#### 4. Next thing to check if the App Registration is using the latest version of the `Client` certificate.
Go to 'chggrd-api-aks-user-prod' App Registration and then to 'Certificates & secrets' -> 'Certificates' tab and make sure the certificate is added and it is has the latest version by checking the Thumbprint.

If the certificate doesn't appear or it has a different Thumbprint, it has to be downloaded from the Key Vault and reuploaded inside the App Registration.


#### 5. Next thing is to check if the dSTS Configuration is still in place.

Go to [Azure Security Configuration Management | fcm-changeguard-test (windows.net)](https://ui.dscm.core.windows.net/dscm/dsts/identity/889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f/uswest2-dsts__dsts__core__windows__net,fcm-changeguard-test?tab=identity) using SAW machine and login with the @ame account.
Check if the subject name is the same as the one in the 'chggrd-client-cer-prod' certificate.

#### 6. Check if the Az Deployer Api is reachable from the tenant and the AKS ip is whitelisted in order to access it.(https://azdeployerapi.trafficmanager.net/AuthenticationMetadata)

#### 7. Restart the pods in the cluster to retrieve the latest version of the certificate strings.
This can be done *either* by:
- Stopping and starting the AKS cluster (*THIS WILL TRIGGER DOWNTIME* of the whole cluster)
- *OR*
- Restarting each service deployment using the command `kubectl rollout restart deployment my-deployment`. This command needs to be repeated for each impacted deployment/service.

#### 8. Test everything to see if the problem is resolved.
Steps:
- Check if the alert is still firing.
- Check the app insights logs to see if failures are still appearing.
- Test using the portal.
- Test using Postman calls to the cluster/services.

