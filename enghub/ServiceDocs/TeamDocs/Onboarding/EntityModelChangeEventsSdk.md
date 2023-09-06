# EntityModel ChangeEvents SDK: Onboarding Client Services
##### (Work In Progress)
</br>

In order for the customers to send `EntityChangeEvents` to the <b>Entity Model Platform</b>,
they need to utilize the [`EntityModel.ChangeEvents.SDK` nuget package](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption/NuGet/EntityModel.ChangeEvents.SDK/versions)
which is available in the [FCM-Consumption](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption) nuget feed.
## Prerequisites
1. Reach out to [`fcmsupport@microsoft.com`](mailto:fcmsupport@microsoft.com) providing the below information to retrieve the `app config endpoint` that is needed to initialize the SDK. 
    1. the use-case
    1. throughput requirements
    1. data-size of each event that the client service will generate based on the schema mentioned below.
    1. Client's service AAD Application Id.

## Schema
1. Below is the example of how to create `EntityChangeEvents`.
   You can find the complete schema [here](https://msazure.visualstudio.com/DefaultCollection/One/_git/EntityModel-ChangeEvents-SDK?path=/EntityModel.ChangeEvent.Schema/src/V1/EntityChangeEvent.cs)
    ```csharp
    private EntityChange BuildEntityChangeEvent()
    {
        EntityChangeEvent entityChangeEvent = new ();
        entityChangeEvent.Timestamp = DateTime.Now;
        entityChangeEvent.StartTime = DateTime.Now;
        entityChangeEvent.EndTime = DateTime.Now;
        ...
        ...
        /* Please refer to the EntityModel.ChangeEvent.Schema.V1.EntityChangeEvent.cs
         * for the official documentation of the properties.
         * This file is available in the EntityModelChangeEventSchema project of the SDK.
         */
        ...
        ...
        entityChangeEvent.ChangeType = EnumExtension
            .GetStringFromValue(ChangeType.AppDeployment);
            
        return entityChangeEvent;
    }
    ```

## Usage
1. Install [`EntityModel.ChangeEvents.SDK` nuget package](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption/NuGet/EntityModel.ChangeEvents.SDK/versions)
   from the [FCM-Consumption](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption) nuget feed.

1. Add this nuget package to your project.
    ```xml
    <ItemGroup>
	  <PackageReference Include="EntityModel.ChangeEvents.SDK" Version= <!--latest--> />
    </ItemGroup>
    ```

1. Add the following code to your project to initialize the SDK:
	```csharp
	EntityModelChangeEventSdk.Initialize<EntityChangeEvent>(services, new InitOptions()
    {
        /* Provide the correct host network value from the ClientServiceHostNetwork enum
         * There are only accepted values: Azure and PF. 
         */
        HostNetwork = ClientServiceHostNetwork.Azure,
            
        /* Provide the correct stage value from the enum corresponding to the stage
         * where the client service is being run.
         */
        Stage = EnvironmentStage.DEV,

        /* Reach out to fcmsupport@microsoft.com to ask for the 
         * correct app config endpoint depending on your stages.
         */
        AppConfigEndpoint = "https://ac-em-appcs-sdk-int-eastus-001.azconfig.io",

        /* Provide this value if the you would want the batches to be published 
         * to the platform automatically after a certain interval.
         * Leave this value to zero if you would want to publish the batches 
         * as they are created. 
         * This value is in seconds. The default value is 0.
         */
        AutoPublishEntityChangesIntervalInSeconds = 5,

        /* Client's can provide their own value for the batch size in bytes.
         * If no value is provided, then SDK configured default value will be used.
         * The batch value should be greater than 24B.
         */
        PublishEntityChangeBatchSizeInBytes = 0,

        /* This is the client's application id in AAD.
         * This is required by the SDK for various resource authentication & telemetry purposes.
         */
        ClientId = "aad-app-registration-client-id",

        /* The azure tenant id where the above app registration is created.
         */
        TenantId = "azure-tenant-id-where-app-registration-is-created",

        /* X509 cert that can be used to authenticate the client id using AAD.
         * Client is responsible for providing a valid certificate which is bound to the AAD App Registration.
         */
         ClientCertificate = <cert>,
    });
	```
    The above step will initialize the SDK and create and weave all the necessary instances using Dependency Injection.
1. Once the initialization is successful, clients can use the singleton bean of type `IPublishEntityChange<EntityChangeEvent>` in their code to publish Entity Changes:
    ```csharp
    public class MyClass 
    {
        private readonly IPublishEntityChange<EntityChangeEvent> _publishEntityChange;

        ...

        public void MyMethod() 
        {
            await _publishEntityChange.PublishEntityChangeAsync(
                new List<EntityChangeEvent>() { /* entity change events */ })
            .ConfigureAwait(false);
        }
    }
    ```
    The above method will create the batches as per the configured batch size and 
    either periodically publish or instantaneously publish the batches depending on the client provided configuration for auto-publishing.

## Error Handling & Retry
 1. Clients need not implement any retry mechanism for this integration. The SDK will handle all the retry logic internally.
    1. When <b>auto-publishing is enabled</b>: 
        1. The SDK will keep trying to publish the batches until the batch is successfully published or the number of failed batches have reached the max limit of 25.
        1. In which case, SDK will throw the underlying exception to the client which can be used to debug. 
        1. Also, the SDK will keep publishing the metrics to FCM team's telemetry for monitoring & alarming purposes.
    1. When <b>auto-publishing is disabled</b>:
        1. The SDK will retry on all common exceptions at most thrice before it fails.
        1. After 3 retries, SDK will throw the underlying exception to the client which can then be used for debugging and engaging [`fcmsupport@microsoft.com`](mailto:fcmsupport@microsoft.com) if needed.
        1. As above, the error metrics will be published to FCM telemetry for monitoring & alarming purposes.

## Troubleshooting
<todo/>

## FAQ
Q . What is the maximum size of the batch that can be published?
</br>
A . The maximum size of the batch that can be published to EntityModel Platform is 50KB. This is the initial limit and can be increased in the future.
</br>
</br>
Q . What auto-publish interval should I configure for my service?
</br>
A . It entirely depends on your business use-case. There are 2 dimensions that client services can use to configure this SDK for best performance and efficiency:
[1.] <b>Batch size</b>
[2.] <b>Auto publish time</b>
</br>
Keep in mind that there is a hard limit of maximum 25 batches that can be staged for publishing.
This means that if the client service has configured an auto-publish time of 5 seconds and the batch count reaches 26 before 5 seconds interval,
SDK will automatically publish the batches without waiting for the entire interval to keep the memory consumption on the client's end in check.
So, the client should configure the batch size accordingly such that their interval & batch size configuration keeps the pending publish batch count less than 25 at any point of time. 
This way there will be no unexpected publishes.
</br>
</br>