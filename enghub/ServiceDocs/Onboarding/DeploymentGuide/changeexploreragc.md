# ChangeExplorerV2 Deployment in AGC

THIS PAGE IS "WORK IN PROGRESS"

This document guides the developer to deploy ChangeExplorerV2 in AGC Environments. There are several steps in this process,some automated and some are manual.

### Deploy Kusto Table and Functions
Kusto Tables, Functions and materialized views are deployed using the release pipeline.
    1. US NAT Release Pipeline - https://msazure.visualstudio.com/One/_release?_a=releases&view=mine&definitionId=37228
    2. US Sec Release Pipeline - https://msazure.visualstudio.com/One/_release?_a=releases&view=mine&definitionId=35622

### Create Lens Explorer Jobs

This will be a manual import into the AGC Lens Explorer Workspace. There are 4 Lens Explorer Scripts we need as part of this deployment.
    - FCM_ChangeExplorerV2_PopulateSimplifiedNetworkTopology_Prod
    - FCMTopologyHydration_Prod
    - Prod - Populate ChangeExplorerLocationExpanded
    - ChangeExplorer_ServiceHierarchySync-PROD: This Job gets data from 

Database Connections needed
    - FCMDC - Connection to FCM Kusto cluster/database

### Create Kusto Orchestrator Job

This will be a manual step. This is the KO job - 'MapChangeEventV1ToV2' from production we need to replicate in AGC.

    1. Here are the steps on how to create the KO Job  - https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/Doc.aspx?sourcedoc=%7B6FABBA9E-8B69-4C67-BC39-3606BCC92857%7D&file=KOJobDocumentation.docx&action=default&mobileredirect=true
    
    2. After creating and running this KO Job, we need create a backfill job with the same parameters, except the start date and time set to 10/01/2022 12:00 AM

### Create App Registrations

Here are the steps on how to create two App Registrations needed for ChangeExplorerV2. 

Create the Apps from App Registration which will be used to login from the front-end and validation of token on the APIM layer using JWT Policy 

#### Create Front-End App in Microsoft Tenant 

1. Search for App Registrations from the Search bar in the Azure Portal, select the app registrations once it shows up in the results 
2. Click on ‘New Registration’ and provide ‘Name-changeexplorerfrontend’, Account Type as ‘Multi-Tenant’, Service Tree ID – Provide FCM Service Tree ID(889acfb9-923f-4e3f-9bf2-2a3f9d95fe4f) 
3. Click on Register. App will be registered and will navigate the user the App Details Page 
4. Click on ‘API Permissions’ under ‘Manage’ on the left navigation of the page. 
5. Click on ‘Add a Permission’. Request API Permissions Page(overlap) on the right side will be opened. 
6. Click on the Microsoft Graph, then click on ‘Delegated Permissions’. In the Select Permissions Search Bar – Type – “user.readbasic.all”. Check box and click ‘Add permissions’. 
7. Navigate to the ‘Authentication’ on the Manage tab.  
    - Click on ‘Add a Platform’->Select Single Page Application. 
    - Add the Redirect URI(example: https://localhost:2000, https://oauth.pstmn.io/v1/callback, etc), select the Access Token and ID Token checkboxes at the bottom. 
    - Click on ‘Configure’ button. 
8. Navigate to the front-end app created from Azure Directory->Enterprise Applications-> search with application id/application name 
9. Select the Properties (left side navigation). Update the Assignment Required to ‘Yes’ and click on Save. 
10. Select the ‘Users and Groups’ on the left side and add the following groups to it: 
    - These are the groups which have access to FCM APP in PROD, need to find similar groups in AGC
        1. All_Alt_Accounts 
        2. All_LinkedIn 
        3. All_MSFTE 
        4. All_MSInterns 
        5. All_MSNonFTE 
11. Raise Admin Consent Request for the roles (user.read and user.read.all).  
    - Go to aka.ms/adminconsent , click on ‘Submit an Admin Consent Request’- Enter the front-end app id created. 
    - Fill out the details 
        - Service Tree Service Name – ‘Federated Change Management’ 
        - Data Classification – Confidential 
        - SDL Link – FCMFC 
        - Request Description and Business Justification – Enter the justification (Eg: ‘ Creating New Front end app for Change Explorer V2. Need Admin consent for the Microsoft users to login using this app id’) 
        - DO NOT CLICK the checkbox ‘Allow Guest Accounts’ 
        - Submit the Request 
        - Follow up with ‘Naveen Duddi Haribabu’ for the Admin Consent Approval 

#### Create Back-End App in Microsoft Tenant 

1. Steps “i” through “iii” are same as ‘Create Front-End App’. Name the backend app as 'changeexplorerbackend' 
2. Click on ‘Expose an API’ and add a scope.  
    - Scopename: user_impersonation 
    - Who can consent: Admin and Users 
    - Admin consent display name: Example: ‘Access Change Explorer API’ 
    - Admin Consent Description: Example: ‘Access Change Explorer API’ 
    - State: Enabled 
    - Click on Add Scope 
3. Click on ‘Add a Client Application’ 
    - Enter the Client ID for the front-end app and chose the authorize scopes (checkbox below the search box) 
    - Click on Add Application 
4. Navigate to Manifest and update “accessTokenAcceptedVersion” to 2 and click on Save. This step is needed for the issuer to be ‘https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47’. If not the issuer of the token will be ‘sts.windows.net’ 


### Deployment of Infrastrucutre, Function Apps, App Service.

ChangeExplorerV2 Infrastructure contains AFD, API Gateways, Azure Function Apps, Azure App Service, Application Insights, Storage, KeyVault. 

Here is the command to run in Powershell to execute the scripts and create the Infrastrucutre and deployment of function apps.

Post Deployment Steps. This is one time Setup.

1. AFD Setup
    - Add the East and West APIM endpoints into the AFD so that AFD can route the traffic to East and West Regions
2. API Gateway Setup
    - Add the Azure Functions to the API Gateway and enable JWT Token Validation
3. Access Setup
    - Kusto: Grant the Kusto access to all the function apps created in the Infrastructure setup
    - Keyvault: Grant the Keyvault access to these function apps -
4. Key Vault Certificates
    - Two Certificates to be created in both east and west key vaults. Here are the details of Certificate from PROD
        1. KV-ICMClientCertificate
            - Subject: CN=icmclient.fcm.msftcloudes.com
            - Subject Alternative Name:  icmclient.fcm.msftcloudes.com
        2. KV-ServiceTreeClientCertProd
            - Subject: CN=servicetreeclient.fcm.msftcloudes.com
            - Subject Alternative Name:  servicetreeclient.fcm.msftcloudes.com
    - One Secret To be created after completing the step 'WebJob to populate Redis Cache for IIP'
        1. ICMPathToServiceTreeIdRedisCacheStorageConnectionString - This will hold the connection to RedisCacheStorage
5. Postman Setup and Testing
    1. Here is the link to the Postman Setup documentation - https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/doc.aspx?sourcedoc={87baf07e-66d5-488e-9ec2-c929c08823c6}&action=edit
    2. Once the Postman is downloded and setup, a new environment is to be created in the postman specific to NAT/SEC. 
        - Environment can be duplicated and update with the environment specific values

### WebJob to populate redis Cache for IIP
IIP uses Azure Redis Cache to find ICM Path to Service ID mapping.
This redis cache is refreshed every 30 minutes via a WebJob.
Below are the important details about this redis cache:
- Redis Cache Name: `fcmazdeployermdscache`
- WebJob that populates this redis cache: `ICMServiceTreeCacher`
- WebApp that hosts this web job: `FCMICMServiceTreeCacher`
- Subscription for these three Azure services: `fbc17084-a3a3-42bf-a9dc-8bc7f996a679`
- Repo code to configure the WebJob: [FCM.ICMServiceTreeCacher](https://msazure.visualstudio.com/DefaultCollection/One/_git/EngSys-ChangeManagement-FCM?path=/src/FCM/FCM.ICMServiceTreeCacher)
- JSON configuration: [Redis Config File](https://paste.microsoft.com/958c4c79-f5d8-4c72-ad37-beecc539c327) 
    | [Webapp Config File](https://paste.microsoft.com/3e0ae450-1031-40dd-85e1-b6d0d01dc79a)
    
    
The cached data is retrieved from Kusto using function: `ICMServiceTreeMapping()`
which uses `ICMToServiceTreeMapping` kusto table.
This table is populated using lens job: [Populate - ICMPathToServiceTree Mapping](https://lens.msftcloudes.com/#/job/394aefcc4f6e4ce7baa7325765bb7613?_g=(ws:cee2f53f-2d2a-40b4-a0c7-a33918652522)).

To use this redis cache in IIP follow the below steps:
1. Create a secret in the IIP KeyVault for the Redis connection string with name = `ICMPathToServiceTreeIdRedisCacheStorageConnectionString`.
2. Verify that this secret name matches with IIP ARM template.
    a. If name is present but does not match, then use the name that is given in the ARM templates.
3. Start to code. [code snippet for reference](https://msazure.visualstudio.com/DefaultCollection/One/_git/FCM-ChangeExplorer-Backend?path=/src/ChangeExplorerV2/IncidentInformationProvider/IncidentInformationProvider/Services/GetIncidentInformationAsyncService.cs&version=GBdevelop&_a=contents)
