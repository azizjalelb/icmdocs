# Sending Change Event Data to FCM FAQs

## I have successfully sent the changes using sample application but don’t see the changes in PPE.
The most common cause for this: 

'EventRouterSample' is not used as ChangeSource. 

If that is not the case, then make sure you are sending the right values as suggested in this documentation. 

Also, FCM PPE is mostly stable but yet it is not production. So, we sometimes make changes to different parts of PPE like API/UI/DB and Event processor. You might be impacted for that and not seeing changes for that. But it should not be for long time. Please try again later and you should see your changes. If you don’t see your changes in FCM PPE for an extended time, then please email fcmsupport. Please provide the externalId when the event was sent and what changes you made to the sample application. 

## I am successfully sending changes using the sample application and can see it in PPE UI but getting errors when I use similar code in another project. 

There are few things that can go wrong: 

- You are using an old version of Event Router. Please get the latest one. 
- You are not initializing the Event router credentials (account. clientId or thumbprint) 
- You are not instantiating Change event correctly with the right values 

## My changes are not showing under my service in FCM PPE UI. 

Please make sure you are doing the following: 

- You are already onboarded to service tree 
- You are already onboarded to FCM 
- You are sending your ServiceTreeGUID in the change event's impactedServiceId field 

## Is the EventRouter API thread safe? 

EventRouter API is thread-safe. Initialize it once and then you can log events through multiple threads. 

## While trying to push data via Change Event Router I noticed that the call OperationalEvents.LogAsync(newList<Ifx.ChangeEvent> { changeEvent }); returns a Task. I was wondering what is the expectation that FCM has regarding how to manage this Task. I realized that to cancel a Task we would need a cancelation token that should be provided to it during its creation. I thus wanted to clarify what expectations FCM has regarding how we should handle Tasks. Our only concern is to not be in a state where we overwhelm the service with multiple Task requests. 

Each batch of events sent from LogAsync can be upto 250KB. If this threshold is breached, then an exception would be thrown, and the caller needs to try again with lesser number of events in the batch. In our testing, we have seen that 10k events of 1KB each translate into a batch size of 160KB, so 10k events per batch could be a good default. To learn more please visit ER documentation:  

https://microsoft.sharepoint.com/teams/WAG/EngSys/AzureAnalytics/Shared%20Documents/EventRouter/Using%20EventRouter%20library%20to%20log%20operational%20data.docx?web=1 

## The system that we use for deploying needs all the dependent packages to be uploaded in VSO associated with our service/product. Thus I would need the .nupkg file of the libraries that FCM needs (I believe it’s Microsoft.Cloud.InstrumentationFramework) so that I can upload it there. 

Platform team publish EventRouter nuget package in wanuget-official repo (Source: http://wanuget/Official/nuget/) by name ‘Microsoft.Cloud.InstrumentationFramework.EventRouter’.  

You can download it and its dependency nuget packages from there and upload to VSO. 

## Can you add (External) Source for us in FCM PPE so that we can send changes in FCM PPE with that External Source? 

Adding a new External Source requires several steps at FCM end and doesn’t add any value in PPE. So, we currently don’t add a new External Source for different services/teams that try sending their changes in FCM PPE. Instead we require you to send changes in FCM PPE with 'EventRouterSample' as ChangeSource and your service tree guid in the impactedServiceId field. Your Source will be added only in FCM Prod. 

## Do we get these events in MDS as well when we send the event to FCM Prod? 

The current IFX agentless doesn’t send the events to MDS and you won’t be able to see the data in Jarvis. However, we send the changes to Kusto and you might be able to use that if you want to explore your data other than FCM UI. For more information on kusto please visit aka.ms/fcmkusto. 

## How do I add application to Azure Active Directory? 

There are plenty of documents online that you can find to guide you how to add your application to Azure Active Directory. One of them is this: 

https://blogs.msdn.microsoft.com/azuredev/2017/03/29/4-ways-of-adding-your-application-to-azure-active-directory/ 

But feel free to follow the documentation you like to add your application to Azure Active Directory. 

## How does FCM authenticate our certificate used by our application to send changes to FCM Prod? 

AAD will do that for FCM. If you are sending using a different certificate that is not associated to the application then AAD will reject the authentication for your application that will fail your changes to come to FCM Prod. 

<!-- ## My deployments/changes are associated with releases.  How can I use release in FCM? 

If you have Deployments/Changes associated with a Release then you should consider sending one ChangeEvent with the 'Release' in the 'Title' field of the ChangeEvent. After that you can send subsequent changes for that as individual ChangeEvent setting their  ExternalParentId field with the SourceRecordId of the ChangeEvent that you sent earlier with the Release (in Title) information. 

Here are all the changes under a specific release '0.7.32.0' in FCM  -->