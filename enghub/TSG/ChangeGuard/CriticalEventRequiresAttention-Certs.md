# Sev2:Fired Application Insights Log [SEV-2] ChangeGuard Critical Event requires attention !!

## Overview

Same resolve as this similar [ICM Incident](https://portal.microsofticm.com/imp/v3/incidents/details/387791153/home).

The Change Guard APIs are deployed as services inside an AKS cluster.
One of the services is a Canary, which initiates calls to all the other services at regular intervals, checking the health
of each one.

One of the reasons the Canary might fail is due to invalid or expired certificates.

> [!NOTE]
> - The TSG for the Emergency Certificate Rotation, with all the details can be found [here](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/ChangeGuard/_layouts/15/Doc.aspx?sourcedoc={b1511488-1e3b-45b8-b1f3-b0b89a26b27a}&action=view&wd=target%28Emergency%20Certificates%20Rotation%20%28ECR%5C%29%20Drill.one%7C970fb975-853c-4b2f-9a7f-12c62a1b988d%2FChange%20Guard%20-%20PROD%20-%20Certificate%20Rotation%20Guide%7C862f4999-13c1-4904-af6a-821e5a8d61d7%2F%29&wdorigin=703).

### Steps taken to investigate the issue:

#### 1. Search for the alert that was fired.
In this case, we search for the ApplicationInsights named `chggrd-api-appinsights-prod`, go to Alerts and check the alert that was fired.
#### 2. Go to query results and investigate the logs.
In this case the logs mentioned that the Canary service can not call the internal Change Assessment service due to an SSL error:
```
"The SSL connection could not be established".
```
Additional information:
```
host:'https://assessment.changeguard.fcm.azure.microsoft.com', path: '
/changeassessment/ev2/00000000-0000-0000-0000-000000000000', query: '' certLocation: '
/app/certs/chggrd-client-cer-prod.pfx', correlationId: '38da412e-6092-471e-a792-78fb14db6f81'
```
#### 3. This led to check if the `Client` certificate used by the Canary service, `chggrd-client-cer-prod`, is valid and has not expired.
The certificate can be found inside the KeyVault: `chggrd-client-cer-prod`.
In this case the latest version of the certificate was not expired.
#### 4. Next thing to check if the Canaries are using the latest version of the `Client` certificate.
For this, we check the Thumbprint of the cert used by the Canary Service.
Use the following query for this, inside the `Application Insights -> Logs`:
```
customEvents
| where timestamp > ago(1d)
| where name matches regex "HttpPostWithClientCertAsync.Certificate.Thumbprint"
| order by timestamp desc
| take 10
| extend ThumbprintInfo = tostring(customDimensions.Message)
```
In this case we can see that the Canary service was using a different version of the Certificate (a different Thumbprint), one that expired the previous day.
We check this by looking at the certificate inside KeyVault, for the version with the previous Thumbprint.

The Canary service loads the certificate at start time (which is when the Kubernetes pod start inside the cluster) at it caches it until the service is restarted.

Since AKS doesn't support getting a Certificate from the KeyVault in PFX format, the workaround is to export the certificate, encode it in base64 and upload the base64 encoded string as a separate Secret inside the KeyVault.
Then the Canary service will retrieve that secret and convert it locally to the PFX format.

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
#### 7. Update the secrets `changemanagerfcmazuremicrosoftcomkeypem` and `changemanagerfcmazuremicrosoftcompem` inside KeyVault with the value of the generated files.
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
#### 8. Restart the pods in the cluster to retrieve the latest version of the certificate strings.
This can be done *either* by:
- Stopping and starting the AKS cluster (*THIS WILL TRIGGER DOWNTIME* of the whole cluster)
- *OR*
- Restarting each service deployment using the command `kubectl rollout restart deployment my-deployment`. This command needs to be repeated for each impacted deployment/service.

#### 9. Test everything to see if the problem is resolved.
Steps:
- Check if the alert is still firing.
- Check the app insights logs to see if failures are still appearing.
- Test using the portal.
- Test using Postman calls to the cluster/services.

