# FCM DataPlatform API Canaries TSG

This alarm will trigger if the Synthetics job that executes the canaries for FCM DataPlatform API is failing; see below for an example.

![Alt text](example_metric_graph_from_jarvis.png)

This could occur     because of several reasons:

1. The service is unavailable (`HttpStatusCode 500`) and there is an availability issue in the service.
2. The response for the given request does not match the expected response (i.e. returning `NoContent 204` rather than `Ok 200`).
3. Metrics emitted during bake time in deployment imply breaking change. The metrics that are being evaluated are availability of FCM DataPlatforms `GetEntityChangeEvent` and `SearchEntityChangeEvent`.

Please execute the following in order:

```mermaid
flowchart TD
    A[Start] --> B{Is the Synthetics Job Running?}
    B -->|No| C[Investigate why the Synthetics Job is not running.]
    B -->|Yes| D{Metrics emitted during bake time?}
    D -->|Yes| E[Check latest deployment in pipeline and initiate rollback if required]
    D -->|No| F{Is the status code returned 500?}
    F -->|Yes| G[Investigate availability of dataplatform APIs, escalate to Sev2 if required.]
    F -->|No| H[Investigate what the returned response is and why this changed from the expected response.]
    click C "https://eng.ms/docs/products/geneva/runners/synthetics/troubleshooting/runtimeissues" _blank
    click E "https://msazure.visualstudio.com/One/_build?definitionId=326385" _blank
    click G "https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/teamdocs/dataplatform/fcm_dataplatform_api" _blank
    click H "https://msazure.visualstudio.com/One/_git/FCM-DataPlatform/pullrequest/8573997?_a=files&path=/tests/ChangeSearchServiceIntegrationTests/IntegrationTestBase.cs" _blank
```

>[!NOTE] The rectangle boxes (or actions) in the flowchart above are clickable links.