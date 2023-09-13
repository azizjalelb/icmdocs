# ChangeGuard - Arcus SDK Authentication Error

## Overview
> [!NOTE] Possible same resolve as this similar [ICM Incident](https://portal.microsofticm.com/imp/v3/incidents/details/387791153/home).

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is Change Assessment, which is used to load BoQ data from Safefly using Arcus SDK nuget package. The authentication is done through the Change Guard's client certificate which is taken from Key Vault.

One of the reasons the Change Assessment might fail is due to invalid or expired certificates.

> [!NOTE]
> - The TSG for the Emergency Certificate Rotation, with all the details can be found [here](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/ChangeGuard/_layouts/15/Doc.aspx?sourcedoc={b1511488-1e3b-45b8-b1f3-b0b89a26b27a}&action=view&wd=target%28Emergency%20Certificates%20Rotation%20%28ECR%5C%29%20Drill.one%7C970fb975-853c-4b2f-9a7f-12c62a1b988d%2FChange%20Guard%20-%20PROD%20-%20Certificate%20Rotation%20Guide%7C862f4999-13c1-4904-af6a-821e5a8d61d7%2F%29&wdorigin=703).

### Steps taken to investigate the issue:

#### 1. Search for the alert that was fired.
In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the alert that was fired.
#### 2. Go to query results and investigate the logs.
In this case the logs mentioned that Change Guard can not call the Arcus Sdk service due to an unauthorized error:
```
"Arcus SDK Authentication Error".
```
Additional information:
```

```
#### 3. This led to check if the `Client` certificate used by the Change Assessment service, `chggrd-client-cer-prod`, is valid and has not expired.
The certificate can be found inside the KeyVault: `chggrd-client-cer-prod`.

If the certificate is expired, it has to be renewed.

#### 4. Next thing to check if the Change Assessment Service is using the latest version of the `Client` certificate.
For this, we check the Thumbprint of the cert used by the Change Assessment Service.
Use the following query for this, inside the `Application Insights -> Logs`:
```
customEvents
| where timestamp > ago(1d)
| where name matches regex "TO_BE_UPDATED"
| order by timestamp desc
| take 10
| extend ThumbprintInfo = tostring(customDimensions.Message)
```
In this case we can see that the Change Assessment Service was using a different version of the Certificate (a different Thumbprint), one that expired the previous day.
We check this by looking at the certificate inside KeyVault, for the version with the previous Thumbprint.

The Change Assessment Service loads the certificate at start time (which is when the Kubernetes pod start inside the cluster) at it caches it until the service is restarted.

Since AKS doesn't support getting a Certificate from the KeyVault in PFX format, the workaround is to export the certificate, encode it in base64 and upload the base64 encoded string as a separate Secret inside the KeyVault.
Then the Change Assessment Service will retrieve that secret and convert it locally to the PFX format.

In this case we need to check if the value inside the Secret points to the newest version of the Certificate.
The Secret name for the cert is `chggrd-client-cer-prod-scrt`.
#### 5. Update the Secret with the new bases64 encoded string of the certificate.
To update the secret with the base64 encoded string version of the latest certificate, download the cert locally using PFX format. 
Convert the cert locally to base64, using the following PowerShell command:
```
$pfxfile = "<pfx-file>"
Set-Content -LiteralPath "chggrd-client-cer-prod.pfx.b64" -Encoding ascii -Value ([convert]::ToBase64String((Get-Content -path "$pfxfile" -AsByteStream )))
```
Update the secret `chggrd-client-cer-prod-scrt` inside KeyVault with the value of the encoded base64 string.
```
#region PROD Environment

 $VaultName = 'chggrd-api-kv-prod'
 $CertName = 'chggrd-client-cer-prod'
 $SecretName = 'chggrd-client-cer-prod-scrt'
 $Subscription_Id = "8830ba56-a476-4d01-b6ac-d3ee790383dc" ## FCMProduction (AME)

#endregion PROD Environment

$PfxFile = "<pfx-file>"
# Create/Set the secret inside KeyVault
$text = Get-Content "$PfxFile.b64" -Raw
$secret = ConvertTo-SecureString -String $text -AsPlainText -Force
Set-AzKeyVaultSecret -VaultName $VaultName -Name $SecretName -SecretValue $secret
```

#### 6. Next check if the `API` certificate used by the ingress service (nginx web server), `chggrd-api-cer-prod`, is valid and has not expired.
The certificate can be found inside the KeyVault: `chggrd-api-cer-prod`.
In this case the latest version of the certificate was not expired.
#### 7. Next thing to check if the ingress service is using the latest version of the `API` certificate.
Download the certificate locally using the PFX format.
Create the .pem and .key.pem files using the following commands:
> [!NOTE] Make sure you have openssl installed locally. It can be installed using chocolatey: `choco install openssl`.

```
  $pfxfile = "<pfx-file>"  
  openssl pkcs12 -in $pfxfile -nocerts -nodes -out changemanager.fcm.azure.microsoft.com.key        
  openssl pkey -in changemanager.fcm.azure.microsoft.com.key -outform PEM -out
  changemanager.fcm.azure.microsoft.com.key.pem       
  openssl pkcs12 -in $pfxfile -clcerts -nokeys -out changemanager.fcm.azure.microsoft.com.crt     
  openssl x509 -in changemanager.fcm.azure.microsoft.com.crt -out changemanager.fcm.azure.microsoft.com.pem
 ```
This will generate the .key and .pem files.
#### 8. Update the secrets `changemanagerfcmazuremicrosoftcomkeypem` and `changemanagerfcmazuremicrosoftcompem` inside KeyVault with the value of the generated files.
```
#region PROD Environment

 $VaultName = 'chggrd-api-kv-prod'
 $Subscription_Id = "8830ba56-a476-4d01-b6ac-d3ee790383dc" ## FCMProduction (AME)

#endregion PROD Environment

$SecretName = 'changemanagerfcmazuremicrosoftcomkeypem'
$text = Get-Content "changemanager.fcm.azure.microsoft.com.key.pem" -Raw -encoding "utf8"
$secret = ConvertTo-SecureString -String $text -AsPlainText -Force
Set-AzKeyVaultSecret -VaultName $VaultName -Name $SecretName -SecretValue $secret

$SecretName = 'changemanagerfcmazuremicrosoftcompem'
$text = Get-Content "changemanager.fcm.azure.microsoft.com.pem" -Raw -encoding "utf8"
$secret = ConvertTo-SecureString -String $text -AsPlainText -Force
Set-AzKeyVaultSecret -VaultName $VaultName -Name $SecretName -SecretValue $secret
```

#### 9. Next thing to check if the App Registration is using the latest version of the `Client` certificate.
Go to 'chggrd-api-aks-user-prod' App Registration and then to 'Certificates & secrets' -> 'Certificates' tab and make sure the certificate is added and it is has the latest version by checking the Thumbprint.

If the certificate doesn't appear or it has a different Thumbprint, it has to be downloaded from the Key Vault and reuploaded inside the App Registration.


#### 10. Next thing is to check if the dSTS Configuration is still in place.

Go to [Azure Security Configuration Management | fcm-changeguard-test (windows.net)](https://ui.dscm.core.windows.net/dscm/dsts/identity/889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f/uswest2-dsts__dsts__core__windows__net,fcm-changeguard-test?tab=identity) using SAW machine and login with the @ame account.
Check if the subject name is the same as the one in the 'chggrd-client-cer-prod' certificate.

#### 11. Check if the Az Deployer Api is reachable from the tenant and the AKS ip is whitelisted in order to access it.(https://azdeployerapi.trafficmanager.net/AuthenticationMetadata)
Please contact mamegh@microsoft.com or AzDeployerDev@microsoft.com for further details on the az deployer side.

#### 12 Restart the pods in the cluster to retrieve the latest version of the certificate strings.
This can be done *either* by:
- Stopping and starting the AKS cluster (*THIS WILL TRIGGER DOWNTIME* of the whole cluster)
- *OR*
- Restarting each service deployment using the command `kubectl rollout restart deployment my-deployment`. This command needs to be repeated for each impacted deployment/service.

#### 13. Test everything to see if the problem is resolved.
Steps:
- Check if the alert is still firing.
- Check the app insights logs to see if failures are still appearing.
- Test using the portal.
- Test using Postman calls to the cluster/services.

More details can be found [here](https://dev.azure.com/msazure/One/_git/FCM-ChangeManager?path=/src/README.md)