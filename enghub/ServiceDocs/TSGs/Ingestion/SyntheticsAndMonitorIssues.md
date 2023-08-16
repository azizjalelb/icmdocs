### Summary
We use [Synthetics](aka.ms/Synthetics) to be able to perform active monitoring on our Ingestion Pipeline. 

Synthetics can have various issues triggering incidents and in this TSG, we go over the most common issues and the process to resolve them

### Issue 1: Kusto client failed due to AAD App Authentication

An excerpt of the log from `RuntimeTraceEvent` looks as below:

```
Child Process: Failed to run job: Microsoft.Azure.Geneva.Synthetics.Runtime.SyntheticsWrapper.CustomerException: Unhandled exception during execution of Synthetic job instance ---> Kusto.Data.Exceptions.KustoClientApplicationAuthenticationException: Kusto client failed to perform AAD application authentication. This is not a Kusto service error. Please review your application credentials.
Full details: 'AADSTS7000222: The provided client secret keys for app 'AAD_APP_ID' are expired. Visit the Azure portal to create new keys for your app: https://aka.ms/NewClientSecret, or consider using certificate credentials for added security: https://aka.ms/certCreds.
```

**Reason:** This error occurs when the Client secret of the AAD App used by Synthetics for authenticating with the Kusto Client expires.

- **AAD App:** *FCMKustoWrite*
- **ClientId:** This can be identfied from the key vaults mentioned in the [config files](https://msazure.visualstudio.com/One/_git/EngSys-ChangeManagement-FCM?path=/src/FCM/Synthetics/EntityModel) using the Secret name - `Secret-MsdialChangeCoreWebApi-KustoApplicationClientId`
- Generate a new `rotating secret` for the application above.
- Update this new secret in the corresponding [config files](https://msazure.visualstudio.com/One/_git/EngSys-ChangeManagement-FCM?path=/src/FCM/Synthetics/EntityModel) for both Prod and PPE under the Secret name - `Secret-MsdialChangeCoreWebApi-KustoApplicationKey`
- Also update this new secret in `FCMINTKV` keyvault to enable testing and debugging effectively.
