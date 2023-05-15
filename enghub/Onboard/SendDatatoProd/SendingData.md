## Register an external source with FCM  

Please chose an external source that represents from where this record is coming from. It’s better to be something generic and short like TFSAzure, MSChange etc. Please also provide a description and source URI (if you have). Source URI is something in the source where anyone can go from FCM UI to see the actual change.  Email fcmsupport with this information. To learn about existing FCM external sources please visit here:  

https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/WopiFrame.aspx?sourcedoc=%7BA5424236-436A-446A-A1CF-62FF563B5B3E%7D&file=FCM%20ExternalSources.docx&action=default  

## Adding your application to Azure Active Directory 

Add your application to Azure Active Directory and provide the ApplicationId and DisplayName to FCM.  

There are many ways you can add your application to Azure Active Directory. Here is a good documentation on it if you already don’t know how to add it: 

https://blogs.msdn.microsoft.com/azuredev/2017/03/29/4-ways-of-adding-your-application-to-azure-active-directory/ 

You can also search online for more documentation on it. FCM needs to add your ApplicationId to FCM prod account for you to be able to send changes to FCM prod using your ApplicationId.  

Make sure your ApplicationId is correctly associated with the cert that you are going to use. Also make sure a servicePrincipal is added for your appId. 

## Daily change volume to FCM estimate 

We also need to know how many estimated changes you are going to send to FCM daily. This is an estimate and please provide that information along with your external source name and certificate information. 

## FCM Prod account information 

When your external source and AAD ApplicationId both are added to FCM PROD then FCM will provide you FCM Prod account information. Then you should be able to send changes to FCM Prod with the following information: 
- FCM Prod Account information
    1. Corp Tenant Application - If your app registration is done in CORP Tenant, then use 'fcmerhub' as fcmprodaccountname in initialization.
    2. AME Tenant Application - If your app registration is created in AME Tenant, then use 'fcmamehub' as fcmprodaccountname in initialization.
- You AAD ApplicationId 
- Certificate Thumbprint associated with your AAD Application 

And the code initialization will look like this: 

<span style="font-family:Courier New; color:orange;">
string thumbprint = "<\certThumbprintAssociatedToYourAADApplicationId>";
 if (! TryGetCertificateByThumbprint(thumbprint, out X509Certificate2 cert))
    {
        throw new Exception("Test certificate not installed or user doean't have access to it.");
    }
OperationalEvents.Initialize( 
    "<\fcmprodaccountname>", 
    "<\yourAADApplicationId>", 
    "cert"); </span>


Timeline for moving to production 

Please allow 5 business days to get all these provisioned from the day both the External Source information and your AADApplicationId are provided.  

FCM also recommends sending your production data to FCM PPE for at least a week so that FCM can validate data conformity and you can see more of your changes in FCM to play with it.  