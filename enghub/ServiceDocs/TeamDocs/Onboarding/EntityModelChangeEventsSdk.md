# EntityModel ChangeEvents SDK: Onboarding Client Services
##### (Work In Progress)
</br>
</br>

In order for the customers to send `EntityChangeEvents` to the <b>Entity Model Platform</b>,
they need to utilize the `EntityModel.ChangeEvents.SDK` nuget package which is available in the [FCM-Consumption](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption) nuget feed.

## Prerequisites
1. Reach out to `fcmsupport@microsoft.com` providing the below information to retrieve the `app config endpoint` that is needed to initialize the SDK. FCM team will 
    1. the use-case
    1. throughput requirements
    1. data-size of each event that the client service will generate based on the schema mentioned below.
    1. Client's service AAD Application Id.

## Schema
1. Below is the example of how to create `EntityChangeEvents`.
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
1. Install `EntityModel.ChangeEvents.SDK` nuget package from the [FCM-Consumption](https://msazure.visualstudio.com/DefaultCollection/One/_artifacts/feed/FCM-Consumption) nuget feed.

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
         * This is required for the SDK to log relevant metrics to FCM telemetry.
         */
        AadApplicationId = "abhinav.test.aad.application.id",
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
            await _publishEntityChange.PublishEntityChangeAsync(new List<EntityChangeEvent>() 
                { /* entity change events */ }
            ).ConfigureAwait(false);
        }
    }
    ```
    The above method will create the batches as per the configured batch size and 
    either periodically publish or instantaneously publish the batches depending on the client provided configuration for auto-publishing.
 
## FAQ
Q . What is the maximum size of the batch that can be published?
</br>
A . The maximum size of the batch that can be published to EntityModel Platform is 50KB. This is the initial limit and can be increased in the future. 