# FCM Data Platform API

| Owner(s): **Andy (andresro@)** | Status: **WIP**          |
|----------------------------|--------------------------|
| Approvers: **TBD**             | Last Updated: **05/12/2023** |

## Contents
- [FCM Data Platform API](#fcm-data-platform-api)
  - [Contents](#contents)
  - [Summary](#summary)
  - [Objective](#objective)
  - [Use Cases](#use-cases)
  - [Requirements](#requirements)
  - [API Design](#api-design)
    - [**GetEntityChangeEvent**](#getentitychangeevent)
        - [Parameters](#parameters)
        - [Responses](#responses)
        - [Example cURL](#example-curl)
        - [GetEntityChangeEvent 200 Response](#getentitychangeevent-200-response)
    - [**SearchEntityChangeEvents**](#searchentitychangeevents)
        - [Parameters](#parameters-1)
        - [Responses](#responses-1)
        - [Example cURL](#example-curl-1)
        - [SearchEntityChangeEvents 200 Response](#searchentitychangeevents-200-response)
  - [Pagination](#pagination)
    - [Stateless Offset](#stateless-offset)
    - [Kusto Stored Query Results](#kusto-stored-query-results)
  - [Versioning](#versioning)
  - [Rate Limiting](#rate-limiting)
  - [Metrics and Alarms](#metrics-and-alarms)
  - [Scalability](#scalability)
  - [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Integration Testing](#integration-testing)
    - [Load Testing](#load-testing)
    - [Canaries](#canaries)
  - [Infrastructure](#infrastructure)
    - [Bicep vs ARM](#bicep-vs-arm)
    - [Uniform Resource Naming Conventions](#uniform-resource-naming-conventions)
    - [Airgap Support](#airgap-support)
    - [Region Agnostic Deployment](#region-agnostic-deployment)
  - [Deployments](#deployments)
  - [Azure Compliance](#azure-compliance)
    - [Authentication](#authentication)
        - [cURL](#curl)
        - [Headers](#headers)
    - [Microsoft URSA Rest API Scans](#microsoft-ursa-rest-api-scans)
    - [OpenTelemetry Audit](#opentelemetry-audit)


<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>

## Summary

This document proposes the low-level design to develop FCM’s Data Platform APIs. The purpose is to evaluate different design choices for the API, highlight requirements and outline tasks that must be completed to comply with functional and non-functional requirements. 

For information regarding the high-level design, see [FCM Data Platform](https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Entity%20Model/Design%20Documents/FCM%20Data%20Platform.docx?d=w07b4c2ca404941f5a4acb334ded64d38&csf=1&web=1&e=5gnhS1). 

## Objective

FCM DataPlatform will create standard APIs that that satisfy the requirements of exposing the [EntityModel](https://microsoft.sharepoint.com/:w:/t/SilverstoneProject/Eeqg50_nDm1ItTXBogvLcq8BybpPWO41X2Yq7FG-UTHlAA?e=Vyla9Q). To support this, we are creating new APIs that adhere to the following: 

- Support the concept of an EntityModel 
- Expose high quality APIs with predefined SLAs. 

## Use Cases

The following are a set of a use cases that these API will address:

1. Client wants to know the risk score for a given deployment; they can use **GetEntityChangeEvents** to find this information.
2. A team wants to build an experience similar to [ChangeExplorerV2](https://changeexplorer.fcm.azure.microsoft.com/home). They can use this set of APIs to expose the standardized `EntityModel`.
3. Client wants to search for all `EntityChangeEvent`s given a specific location. They can utilize **SearchEntityChangeEvents** to find this information. Similarly, they can use other search criteria to find `EntityChangeEvent`s.
4. Client has an incident. Given search criteria, they want find all `EntityChangeEvent`s within a given time frame and rank them by risk score. Utilizing **SearchEntityChangeEvents**, they can execute this search. 

## Requirements

The technical requirements are: 

- Each API must be highly available and horizontally scalable.  
- Every component must have its own test base, health monitors & alarms. The health monitors and alarms must be generated via code.
- APIs must be deployable in automated fashion meeting coding, deployment, monitoring and security best practices. 
- Infrastructure management must be standardized and source controlled across components.
- All APIs must be compliant with Azure policies (see [Azure Compliance](#azure-compliance) section).
- All APIs must have integration and load tests for INT, PPE and PROD environments. 
- APIs must be versioned and backwards compatible. API override is not supported. 
- Design docs and TSGs will be onboarded to [Engineering Hub](https://msazure.visualstudio.com/One/_git/FCM-Engineering-Hub). 

## API Design

### **GetEntityChangeEvent**

**`GET`** /v1/entityChangeEvents?changeActivityId={<g>**ChangeActivity**</g>}&entityId={<g>**EntityId**</g>}

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `ChangeActivity`  |  required | string         | Unique Id from the source that tracks the deployment.        |
> | `EntityId`        |  required | string         | Location Id of the deployment.       |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | `EntityChangeEvent`; [see below](#getentitychangeevent-200-response)                                    |
> | `204`         | N/A                               | N/A                                                                 |
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                             |
> | `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}`                            |
> | `404`         | `application/json`                | `{"code":"404","message":"Not Found"}`                               |
> | `429`         | `application/json`                | `{"code":"404","message":"Too Many Requests"}`                              |
> | `500`         | `application/json`                | `{"code":"500","message":"Internal Server Error"}`                   |
> | `503`         | `application/json`                | `{"code":"503","message":"Service Unavailable"}`                     |

##### Example cURL

> ```javascript
>  curl -X GET https://fcmdp.azurefd.com/v1/entityChangeEvents?changeActivityId={ChangeActivity}&entityId={EntityId}
> ```

##### GetEntityChangeEvent 200 Response
>```json
>{
>    "SchemaVersion": "string",
>    "Timestamp": "datetime",
>    "StartTime": "datetime",
>    "EndTime": "datetime",
>    "EntityType": "string",
>    "EntityId": "string",
>    "ChangeType": "string",
>    "Payload": "string",
>    "ChangeActivity": "string",
>    "MetaData": "dynamic",
>    "Source": "string",
>    "PlannedInterruption": "string",
>    "ImpactDuration": "int",
>    "ChangeOwner": "string",
>    "ChangeOwnerType": "string",
>    "ParentChangeActivity": "string",
>    "ChangeState": "string",
>    "EntityCorrelationResult": {
>        "LastUpdatedTime": "datetime",
>        "Score": "double",
>        "MeasureCategory": "string"
>    }
>}
>```

### **SearchEntityChangeEvents**

**`GET`** /v1/entityChangeEvents?startTime={<g>**StartTime**</g>}&endTime={<g>**EndTime**</g>}&entityId={<g>**EntityId**</g>}&serviceTreeId={<g>**ServiceTreeId**</g>}&pageSize={<g>**PageSize**</g>}&offset={<g>**Offset**</g>}&sortBy={<g>**SortBy**</g>}

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `StartTime`       |  required | datetime       | Start time of `EntityChangeEvent` search. Max 1 week range with `EndTime`.       |
> | `EndTime`         |  required | datetime       | End time of `EntityChangeEvent` search. Max 1 week range with `StartTime`.     |
> | `EntityId`        |  At least one of `EntityId` or `ServiceTreeId` must be used. | string         | Location Id of the deployment.       |
> | `ServiceTreeId`   |  At least of `EntityId` or `ServiceTreeId` must be used.  | string         | [ServiceTreeId](https://microsoftservicetree.com/home) to utilize for search.     |
> | `PageSize`        |  optional | int         | Page size of results to return. Defaults to `50`; max `1000`.     |
> | `Offset`        |  optional | int           | Offset to calculate next set page of results. Defaults to `0`.    |
> | `SortBy`          |  optional | string         | Location Id of the deployment. Defaults to `StartTime`.    |

Multiple **```EntityId```** and **```ServiceTreeId```** can be searched, up to a maximum of 10 each. Syntax is ...entityChangeEvents?entityId={<g>**EntityId**</g>}&entityId={<g>**EntityId**</g>}entityId={<g>**EntityId**</g>}...&serviceTreeId={<g>**ServiceTreeId**</g>}&serviceTreeId={<g>**ServiceTreeId**<g/>}...

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | List of `EntityChangeEvent`s; [see below](#searchentitychangeevents-200-response)                                     |
> | `204`         | N/A                               | N/A                                                                 |
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                             |
> | `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}`                            |
> | `404`         | `application/json`                | `{"code":"404","message":"Not Found"}`                               |
> | `429`         | `application/json`                | `{"code":"404","message":"Too Many Requests"}`                               |
> | `500`         | `application/json`                | `{"code":"500","message":"Internal Server Error"}`                   |
> | `503`         | `application/json`                | `{"code":"503","message":"Service Unavailable"}`                     |

##### Example cURL

> ```javascript
>  curl -X GET https://fcmdp.azurefd.com/v1/entityChangeEvents?startTime={StartTime}&endTime={EndTime}&entityId={EntityId}&serviceTreeId={ServiceTreeId}&pageSize={PageSize}&offset={Offset}&sortBy={SortBy}
> ```

##### SearchEntityChangeEvents 200 Response
>```json
>{
>    "Count": "int",
>    "SortBy": "string",
>    "Offset": "int",
>    "EntityChangeEvents": [
>        {
>            "SchemaVersion": "string",
>            "Timestamp": "datetime",
>            "StartTime": "datetime",
>            "EndTime": "datetime",
>            "EntityType": "string",
>            "EntityId": "string",
>            "ChangeType": "string",
>            "Payload": "string",
>            "ChangeActivity": "string",
>            "MetaData": "dynamic",
>            "Source": "string",
>            "PlannedInterruption": "string",
>            "ImpactDuration": "int",
>            "ChangeOwner": "string",
>            "ChangeOwnerType": "string",
>            "ParentChangeActivity": "string",
>            "ChangeState": "string",
>            "EntityCorrelationResult": {
>                "LastUpdatedTime": "datetime",
>                "Score": "double",
>                "MeasureCategory": "string"
>            }
>        }
>    ]
>}
>```

## Pagination

There are two approaches to tackle pagination. We will present both here but are opting for the stateless option.

### Stateless Offset

For the stateless option, we will utilize an `Offset` value to calculate the number of records we will skip to start returning results to the client. We will pass the parameter into our database solution (currently Kusto); example below:

```sql
.create-or-altar SearchEntityChangeEvents(StartTime: datetime, EndTime: datetime, EntityId: dynamic, ..., Offset: int, PageSize: int, SortBy: string) { 
EntityChangeEventMaterializedView
    | where StartTime between ...
    .
    .
    .
    | sort by SortBy
    | where _row > Offset
    | take PageSize
}
```

The benefits of this option are that:

1. We don't have to maintain stored query results in a storage account. Based on user patterns, these might expire often or not be used. 
2. Additionally with (1), we would have to come up with an expulsion mechanism to clean old records.
3. Since this set of API does not have complex queries, we assume that the query time will be low, so rerunning queries should have minimal effect on performance. 


### Kusto Stored Query Results 

Our data lives in Azure Data Explorer (Kusto). Therefore, it would be beneficial to store query results using ADX's built in functionality [Stored query results](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/stored-query-results). Below is an example of the workflow:

```sql
.set stored_query_result StoredQueryResultName <| SearchEntityChangeEvents(...);
stored_query_result("StoredQueryResultName")
| where Idx between(StoredQueryResultOffset .. PageSize)
```

Some of the limitations of this are:

- We can't exceed 500 columns; otherwise the stored query results cannot be saved. This is not an issue given the **EntityChangeEvent** model. 
- The query results are saved to a storage account associated with the cluster. If we implement a distributed Kusto cluster and cache for our data, we would have to revisit the complexity of using the built in tools.
- Stored query results last up to 24 hours and can be access by the same service principle. If we find ourselves using an large amount of storage space, we can run a job that clears stored query results in excess of N minutes, likely 15 or 30. 

## Versioning

Generally, we have the following strategies available to version our API:

1. URI path
2. Query parameter
3. Custom header

For this set of APIs, we will utilize **URI path** versioning (easiy debugable, less prone to breaking changes, readily modifyable). We will also support past versions of the API up to 1 year before deprecation. For API deprecation, we will create a campaign to support onboarding to the newer version.

## Rate Limiting

Rate limiting will be handled by an [APIM](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts) layer that sits behind our [Front Door](https://azure.microsoft.com/en-us/products/frontdoor). Since our authentication method will utilize AAD compliant bearer tokens, we will opt for a [rate limit policy set by key](https://learn.microsoft.com/en-us/azure/api-management/rate-limit-by-key-policy) and return a `429` **Too Many Requests** message on exhaustion. See below for an example inbound rule:

```json
<policies>
    <inbound>
        <base />
              <rate-limit-by-key calls="10"
                renewal-period="60"
                counter-key="@(context.Request.Headers.GetValueOrDefault("Authorization","").AsJwt()?.Subject)" />
    </inbound>
    <outbound>
        <base />
    </outbound>
</policies>
```

>[!NOTE]
> Should we utilize the bearer token as part of the authorization header as the `rate-key` or something else?

## Metrics and Alarms

Metrics will be auto-configured via [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview?tabs=net) on all http triggered functions; we will refrain from creating custom logs and metrics whenever possible. On cases where custom metrics are required (such as individual method processing time), we will utilize a dependency injected `ILogger` interface applicable to [isolated process azure functions](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#logging) to emit the log for alert triggering.

Alarms will be configured utilizing either (1) built in metrics or (2) custom log metrics via [Alert Rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview). These alerts will be configured through ARM templates; for further reading, see the [metricAlerts](https://learn.microsoft.com/en-us/azure/templates/microsoft.insights/2018-03-01/metricalerts?pivots=deployment-language-arm-template) documentation. Since email notification is not a sufficient alerting mechanism, we will utilize the **FederatedChangemanagement-AzureMonitor** ICM connector to generate ICM incidents as part of the alert rule's action group. For further reading on how this is set up, see [Azure Monitor ICM Connector](https://eng.ms/docs/products/icm/developers/connectors/icmaction).


## Scalability

We will utilize isolated out-of-process Azure Functions on a premium plan hosted on Azure. For more details, see [Azure Functions hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) and the [ChangeExplorerV2 HLD](https://teams.microsoft.com/_?culture=en-us&country=us#/apps/d7958adf-f419-46fa-941b-1b946497ef84/sections/MyNotebook) for pros and cons. Additionally, a dedicated or premium plan is required for serverless logging to Geneva/Jarvis.

> Since we are designing this as a high TPS system, what are the limits of a distributed serverless implementation? Assuming we run on Windows, we can expecte 100 instances at 400 ACU capacity. This is ideal for high throughput systems with small code executions.

## Testing

### Unit Testing

All code must be unit tested and code coverage reports must be a pre-requisite of pull request approver. We use the following as guidelines:

- Continued use of NUnit3 as our preferred testing suite. Previously, we implemented very verbose unit tests via Mock packages, but the recommendation moving forward is to utilize tools such as [Autofixture](https://github.com/AutoFixture/AutoFixture) to arrange our test cases to avoid writing big tests.
- Write small, testable functions; extract large methods into smaller helper methods. Test behavior, not implementation. 
- Install [GitHub Copilot](https://github.com/features/copilot) and utilize it to write tests. There is a directive from senior leaderships to utilize AI-powered tools to increase our productivity.
- Add code coverage for pull requests. For more info, see [code coverage for pull requests](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/codecoverage-for-pullrequests?view=azure-devops).

### Integration Testing

From documentation, it seems that utilizing the built in Test Plan feature of Azure DevOps is the way to run integration tests (such as with this guide here: [Run Automated tests from test plans](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops)); however, I am open to suggestions on this.

>[!NOTE]
> Are there any better solutions for integration testing? Ideally, the solution would be easily integrated with an ADO release pipeline. 

### Load Testing

For load testing, we will employ the use of [Azure's load testing service](https://azure.microsoft.com/en-us/products/load-testing/) to determine performance and bottlenecks with our services. A couple of things to observe:

- For load testing, we have two options: either creating a simple GUI based test via the portal with limited configurability or creating a [JMeter load test](https://learn.microsoft.com/en-us/azure/load-testing/how-to-create-and-run-load-test-with-jmeter-script) via JMeter script. Since our team has experience with the latter and it is highly configurable, we will utilize the second option.
- Load testing will be part of our CI/CD pipeline. This is to ensure that we don't introduce regressions in the form of performance or availability to our application on deployments. For further reading, see [automating load tests with CI/CD](https://learn.microsoft.com/en-us/azure/load-testing/tutorial-identify-performance-regression-with-cicd?tabs=pipelines).

### Canaries

Logs and metrics are emmitted to application insights. Because of this, we can utilize the built in [standard test](https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability-standard-tests#create-a-standard-test) feature to create REST calls to our backend at a configured interval. We can configure our success criteria to be just the status code returned (such as `200 OK`) or a content match (such as a specific json string for an `EntityChangeEvent` object). Alternatively, we can create a cron triggered function that invokes our REST APIs at a configured interval and use the [TrackAvailability](https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability-azure-functions) feature to determine service health.

>![NOTE] Is there a better way to run canaries? Would prefer a native solution.

## Infrastructure

### Bicep vs ARM

>[IMPORTANT!] After conducting a PoC to determine the viability of utilizing Bicep with EV2, we will decline this option for now and opt for region agnostic conforming ARM templates. EV2 does not natively support Bicep files, which would require us to create ARM templates at build time. This works, but given that (1) our auxilary parameter files are configured for use with the region agnostic model and that (2) Bicep currently doesn't provide an inline solution for parameter population it becomes quite cumbersome to work with both of these at the same time. Thus, we will for now utilize ARM templates and will wait for further support to be released.

We utilize ARM templates and EV2 deployments as our infrastructure solution for deploying our code. Moving forward, we will make it a P0 goal to utilize [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep) to deploy our infrastructure. In essence, Bicep is infrastructure as code; it's Azure's response to AWS's CDK or HashiCorp's Terrraform. For benefits, please see the difference between writing an ARM template vs writing an equivalent [Bicep file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-bicep?tabs=CLI).

> Does EV2 support Bicep? No, EV2 (EV2 MSInternal, i.e. the build step in ADO release pipelines that deploys our code) currently does not natively support Bicep files, although it is in their roadmap to support. To circumvent this, we will generate ARM template file equivalents as a build step in our pipeline until the EV2 natively supports Bicep. For further reading, see this [internal stackoverflow post](https://stackoverflow.microsoft.com/questions/263321).

### Uniform Resource Naming Conventions

One mistake we made with ChangeExplorerV2 is that we deployed resources into production without agreeing on naming conventions. This caused some heartache as we introduced more components into the system, as everyone had their own way of naming resources. Moving forward, we will come to an agreement on what best practices to follow when naming resources so we avoid this issue in the future. Some best pratices for azure can be found in [define your naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming).

### Airgap Support

TOOD: Vamshi will provide an example to me next day. 


### Region Agnostic Deployment

Given the findings in [Bicep vs Arm](#bicep-vs-arm), we will create region agnostic model ARM templates for deployments. Creating these models is defined [in this Ev2 guide](https://ev2docs.azure.net/getting-started/tutorial/add-resources/arm-template.html). Examples of region agnostic models already in use in FCM can be found in this [`RegionAgnosticModel`](https://msazure.visualstudio.com/One/_git/FCM-ChangeExplorer-Backend?path=/.deploy/RegionAgnosticModel&version=GBmain&_a=contents) folder.

## Deployments

We will generate four (4) different pipelines:

- FCM-DataPlatform-Backend-PullRequest: A build pipeline that is triggered whenever a new pull request is submmited to the ```develop``` branch. It's purpose it to validate that a pull request meets our team's requirements (such as code coverage, load tests, etc) to be merged. *squash merge* for all successful pull requests.
- FCM-DataPlatform-Backend-Official: A build pipeline that is triggered whenever a change is merged into ```main```. *Basic merge* so that changes can be moved from ```develop``` into ```main``` easily with a single pullrequest.
- FCM-DataPlatform-Backend-INT: A release pipeline that deploys our code to Azure using EV2. This solely deploys to our INT subscription and does not require the use of approval. 
- FCM-DataPlaform-Backend-PPE/PROD: A release pipeline that deploys our code to Azure using EV2. This deploys to our PPE environment first and requires approvals authenticated with JIT for our PPE and PROD subscriptions. 


## Azure Compliance

### Authentication

FCM DataPlatform APIs will be enrolled via app registration. Authentication will initially be single tenant (Microsoft) via [Azure AD](https://azure.microsoft.com/en-us/products/active-directory) with support for multi-tenant in the future if required. Bearer tokens will be generated and sent with API calls as an `authorization` header; example below:

##### cURL
> ```javascript
>  curl -X GET -H "Authorization: Bearer {AccessToken}" https://fcmdp.azurefd.com/v1/entityChangeEvents?changeActivityId={ChangeActivity}&entityId={EntityId}
> ```

##### Headers

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `AccessToken`  |  required | string         | Bearer token granted after AAD authentication; single tenant       |

>[!NOTE]
> Should we support additional authentication methods, such as certificate based authentication?

### Microsoft URSA Rest API Scans

All REST APIs must be onboarded to the [URSA Web Scanner](https://eng.ms/docs/microsoft-security/security/azure-security/security-health-analytics/unified-remote-scanning-ursa/ursa-web-scanner/onboard/apionboard) for compliance reasons. ChangeExplorerV2 rest APIs are already onboarded onto the platform, so we will utilize the same access resources in each environment (i.e. ```URSAWebScannerSecretUri```) for authentication. Scans will be executed **on a monthly cadence as default**, but we can choose to execute them as part of our CI/CD pipeline by triggering an immediate scan through the [URSA API](https://ursa.trafficmanager.net/swagger/index.html).


### OpenTelemetry Audit

As part of Microsoft's effort to maintain security audit logs, we will onboard all of our applications (in this case Antares based) to emit audit logs through [OpenTelemetry logging](https://eng.ms/docs/products/geneva/collect/instrument/opentelemetryaudit/overview). We have already onboarded ChangeExplorerV2 components to OpenTel, so this would be a continuation of that. A couple of remarks:

- ChangeExplorerV2 APIs were **read** only; if this pattern continues then our logging should be minimal (i.e. log what are application is accessing). If our APIs allow modification of resources or execute privileged actions as defined in the OpenTel doc, we will need to evaluate our workflow to ensure we audit all related instances.
- Since Geneva Agents (GAs) are tied to service plans for Antares based apps, we will need to create a separate service plan only for use by our DataPlatform APIs.
- We will generate a new namespace in our Geneva Logs account for each environment, i.e. ```fcmdataplatformint```.