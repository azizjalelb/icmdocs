# Deployment Guidance

## Purpose

The purpose of this document is to outline fundamental practices we must employ as part of our deployments for FCM components. Before deploying a component, ensure that it meets the following requirements so that we can ensure a high level of confidence and deliver a stable product to our customers. 

- Key takeaways:
    - Ensure that all code is unit tested and approved by at least two people.
    - Ensure that pipeline builds are always healthy and building.
    - Strive to achieve >90% code coverage. 
    - Address any vulnerabitlies as part of codeql.
    - Release gradually from int to ppe to prod.
    - For prod deployments, release in order of canary, pilot and then region pairs with a minimum 4 broad/heavy regions. 
    - Allow the SDP mandated baketime in between deployments.
    - Only deploy using RA Ev2; do not deploy using Ev2 classic.
    - Scrutinize one way door deployments. Sync up with stakeholders to ensure no interruption to clients.
    - Ensure there is an effective rollback mechanism in place. Test it dev and ppe environments before deploying to prod.
    - Ensure that every component has integration tests built into the release pipeline.
    - Do not deploy on a Friday.
    - Create a canary to constantly invoke our service and ensure availability/latency metrics are stable.
    - Utilize a Manual Change Management (MCM) template to document manual testing. 
    - Monitor relevant dashboards to ensure that key metrics, like availability or latency, aren't negatively impacted by the deployment.
    - Ensure that alarms are functional and ICM tickets arising from the deployment at Sev2 priority.
    - DRI is not responsible for monitoring the code. The implementor must ensure successful deployment to the last region.

> [!NOTE] 
> This document will be periodically reviewed and updated with the latest best practices.

## Requirements

### Code Requirements

#### PullRequests:

- All pull requests must have [work items linked](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-link?view=azure-devops) to ensure proper tracking.
- Minimum of [two approvers](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser) to merge; this is set by default as a branch policy to `develop` and `main`.
- All comments must be resolved, including nits. For larger tasks that are outside of the scope of the PR create backlog tasks and link them accordingly.
- If a merge to `main` occurs, the deployment to production must be executed immediately to avoid code buildup when syncing from `develop`.
- As part of the PR, the code must build using the `<REPO>-PullRequestBuild` pipeline.

#### Builds:
- Any code merged into the `develop` and `main` branches must build using it's appropriate build pipeline i.e. **PullRequest** or **Official**.
- As part of the build, all vulnerabilities must be indexed and uploaded to [codeql](https://liquid.microsoft.com/Home/Support?copilot=1). Remediate these vulnerabilities as flagged by the tool. *Note that this is done automatically as part of S360*.
- Ensure that `develop` and `main` pipelines always build prior to merging code; *do not merge code if the pipeline is broken*. Create a separate PR to address the broken build and ensure it's success before merging code updates. 
#### Unit Tests:
- Ensure that any code component has unit tests implemented, typically in [nuint](https://nunit.org/) for C# packages.
- If a code component does not have unit tests, call it out during standup. Do not wait for someone else to create a skeleton test framework; generate your own. Seek help if you're unsure on how to do this. 
- All tests must run and pass; *do not comment out failing tests or change test criteria to get a successful build*.
- [Test behavior, not implementaiton](https://nunit.org/).
- If testing proves difficult, consider refactoring the code on critical flows to allow more granular testing.
- When reviewing a code PR doesn't have unit tests added/modified, ask why. Let's make it a habit to properly unit test all code.

#### Code Coverage:
- As part of builds ensure that [code coverage](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/review-code-coverage-results?view=azure-devops) is emmitted, usually VSTest or XPlat.
- Azure guidance has a requirement for [pr code coverage diff](https://eng.ms/docs/cloud-ai-platform/azure-core/azure-core-docs/development-cycle/test/code-coverage), specifically >50% for lines of changed code with a northstar of >80%.
- Internal team goal is code coverage of >90% on all branches with the aforementioned guidelines for PR code diff. 

#### Code Quality
- Code quality is tracked by [codeql](https://liquid.microsoft.com/Home/Support?copilot=1) as well as other automated systems within the ADO pull request. Address these quality concerns on a case by case basis.
- Vulnerabilities (such as updating NUGET packages) must be addressed at Sev2 severity as they are an attack vector on our system and typically an S360 flag.
- Hollistically check code on a regular basis; ask yourself if it makes sense/can be improved. Discuss with team during oncall and create a backlog to address the issues.


### Releases

#### ADO Release Pipeline

- Link releases pipelines to [OneBranch](https://eng.ms/docs/products/onebranch/onebranch). For `Production` pipelines this is mandated.
- There must be two pipelines per repo:
    - The first pipeline deploys **development** code to a dev/int environment in the MSFT tenant.
    - The second pipeline deploys **production** code to a ppe and prod environment in the AME tenant.
- If pipelines are not CI/CD, all deployments must be [manually triggered](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/triggers?view=azure-devops). This includes the dev environment.
- For deploying POC code, consider generating a [buddy release](https://eng.ms/docs/products/onebranch/release/yamlreleasepipelines/manageyourpipeline) to deploy resources. This helps avoid issues with deploying potentially system breaking changes to the dev environment.
    - As an additional requirement, ensure all resources deployed with the above release are deleted if no longer in use; *do not leave stale/unused resources running as this creates operational overhead*.
- Segment releases to the most granular locations possible; typically for FCM this is at the region level. More on this later.

#### ARM Templates

- Require all changes to be deployed via [Ev2](https://ev2docs.azure.net/getting-started/overview.html) ARM templates.
- Do not use `ev2 classic` for ARM deployments; this is on deprecation. All components, unless marked for deprecation, must be deployed using [region agnostic](https://ev2docs.azure.net/references/api/new-ra-rollout.html?q=region%20agnostic) (RA) Ev2.
- Configure a minimum wait time/bake time when deploying changes; this is automatically configured as [1 day for deployments to the `prod` environment](https://ev2docs.azure.net/features/rollout-orchestration/managed-validation/overview.html?q=managed%20valida) through SDP.
    - Emergency deployments can have this setting overriden.
- Ev2 deployments through the pipeline will be `code` deployments (i.e. deploying bits to existing infrastructure). `infra` deployments (i.e. deployments that set up resources for the first time in a subscription) can be executed using the CLI. These are typically ran only once and not again.

#### Regional Deployment

- Ensure that we are using [Safe deployment practices](https://ev2docs.azure.net/getting-started/sdp.html?tabs=regions) in all of our rollouts. 
- Utilize **region based progression** for all rollouts:

| Stage | Name    | Regions                                                                                   | Sequence                 |
|-------|---------|-------------------------------------------------------------------------------------------|--------------------------|
| 1     | Canary  | Central US EUAP, East US 2 EUAP                                                           | Serial (these two regions are paired) |
| 2     | Pilot   | West Central US, East Asia                                                                | Parallel or serial       |
| 3     | Medium  | UK South                                                                                  |                          |
| 4     | Heavy   | East US                                                                                   |                          |
| 5     | Broad 1 | 1st region of all public region pairs, public 3+0 regions, USDoD Central (FF), China North (MC), USNat East (US Nat), USSec West (US Sec) | Parallel or serial       |
| 6     | Broad 2 | 2nd region of all public region pairs, public 3+0 regions, USDoD East (FF), China North 2 (MC), USNat West (US Nat), USSec East (US Sec) | Parallel or serial       |
| 7     | Broad 3 | 1st region of all remaining region pairs (FF / MC / US Nat / US Sec), remaining 3+0 regions (FF / MC / US Nat / US Sec) | Parallel or serial       |
| 8     | Broad 4 | 2nd region of all remaining region pairs (FF / MC / US Nat / US Sec), remaining 3+0 regions (FF / MC / US Nat / US Sec) |                          |

- Ensure we deploy in the following order:
    - Deploy to the canary region `east us 2 euap` (stage 1).
    - Deploy to the pilot region `west central us` (stage 2).
    - Deploy to the heavy region `east us` (stage 3).
    - Deploy to the broad region `west us` (stage 4, region pair of `east us`).
    - Deploy to the broad regions `east us 2` and `central us` (region pairs).
    - For stage 5+ in highly scaled systems, deploy in [region pairs](https://eng.ms/docs/cloud-ai-platform/azure-core/azure-networking/sdn-dbansal/azure-virtual-network-manager/azure-virtual-network-manager/devops/environments/public/region-pairing) as required.
- We must at minimum deploy our service to 1 canary, 1 pilot and 4 heavy/broad regions. All regions must be region paired.
- Bake time is mandated by SDP and auto configured; *do not bypass this* by triggering a secondary stage on the pipeline.
- Ensure that tasks [require successful prior deployment](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/releases?view=azure-devops) to continue fan out.
    - For example, pilot region will require a successful deployment to the canary and the heavy region will require a successful deployment of the pilot, etc.
- **Do not execute deployments on Friday**. Deployments on Friday will require the DRI to address any incoming tickets that might be related to the deployment. Deploy on any other weekday during business hours.

#### Rollbacks

- Before executing a deployment, ask yourself if it is a [one way or two way door](https://medium.com/one-to-n/one-way-two-way-door-decisions-a0e29029e200) deployment.
    - A one way door deployment can be thought of as irreversiable process (i.e. deploying a fixed API contract that clients will depend on).
    - A two way door deployment can be thought of as a reversible process (i.e. updating a config value to point to a different database).
- Deployments that are one way require increased scrutiny as other teams are dependent on them. For these types of changes, **ensure that you deploy in a way that does not break existing usage by clients, such as API versioning**. 
- Deployments that are two way always have rollbacks which are the ability to revert back to a known good state. Effective rollbacks are characterized by their ease of execution and fast recovery into the known good state. They should not be complicated to execute nor take an arbitarily long time to revert.
- **Before a deployment, familiarize yourself with the rollback mechanism and test it the dev and ppe environments before continuing deployment to prod**.
    - As an example, a lot of FCM's code is deployed to Azure Functions. We have opted to utilize a standard [app slot swap rollback](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots?tabs=portal) that is a built-in feature of functions to quickly help rollback any code change that is causing issues.
- **Rolling back problem changes should almost always be the first course of action taken when a problem arises**. In some cases, rolling forward is preferred (i.e. emergency deployment to fix a bug) although this will require manager approval. 


### Validation

#### Integration Tests

- All components must have integrations tests built directly into the release pipeline as part of the deployment. This can be done using [vstest on ado](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops) although simpler solutions, such as generating a `*_IntegrationTests.dll` package and executing it will suffice.
    - As an example, take a look at the integration tests created for [ChangeSearchService in DP platform](https://msazure.visualstudio.com/One/_git/FCM-DataPlatform?path=/tests/ChangeSearchServiceIntegrationTests).
- When deploying new code, add integration tests to validate the deployed changes output the expected behavior. If modifying paths that impact existing code ensure that integration tests succeed locally before continuing with the deployment. Any test failing should be addressed as part of the PR.
- If integration testing fails do not continue the deployment. Fix the tests in a PR.

#### Canary

- Consider creating a canary to periodically invoke our services.
    - Canaries are useful in ensuring that traffic is always flowing into our services, even those that are not used often or have yet to be adopted (such as `Payload2Build`).
- Segment canary traffic into it's own dashboard to distinguish it from regular customer traffic and not introduce noise to genuine service calls.

#### Manual Tests

- If integration tests are not present or the changes deployed cannot be tested in that manner, employ a manual test using the [Manual Change Management](https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Engineering%20Excellence/MCMs/2024/July/FCM%20Manual%20Change%20Management%20%E2%80%93%20Update%20APIM%20Configs%20for%20DP.docx?d=wc7639d48aa284c82b5cc67e13716bdd0&csf=1&web=1&e=IXfu3R) template.
- Document every test case that will be executed and document it's success/failure to ensure proper tracking.
- Have this document and the deployment procedure review by the DRI prior to deployment into the AME tenant.  

### Monitoring

#### Dashboards

- Before deploying, ensure that you have access to the relevant metrics and logging for the services you are deploying. The key points of interest to look for are:
    - **Availability**: Is there an increase in server errors after code was deployed? If yes, **rollback immediately**.
        - Stable systems, especially those constructed as highly scaleable in the cloud, generally don't fail. Consider any minute uptick in failures as critical.  
    - **Latency**: Has the time for requests to be serviced after deployment increased significantly? If yes, **rollback immediately**.
        - Note that significantly is semi-arbitrary here; we should compare this value at P95.
    - **Exceptions**: Am I receiving more exceptions as part of a code deployment? If yes, **rollback immediately**. 
        - Exceptions can still occur in successful requests via retries. We should consider an uptick in this a failure.
    - **CPU/memory usage**: Has the CPU and/or memory usage increased? Consider if this is siginificant enough to cause degradation in the other metrics.
        - We heavily rely on [kusto](https://azure.microsoft.com/en-us/products/data-explorer) as our database of choice. Monitor the [cluster performance dashboard](https://learn.microsoft.com/en-us/azure/data-explorer/using-metrics) to ensure that it is healthy.
- **Monitor dashboards for one day after deployment completion**. A deployment can be considered **complete** after having been deployed for at least one day in the last stage.

#### ICM Queue

- All of our service components should have alarms configured to alert our team in case of degradation. **Validate that these alarms are working as expected before deployment**.
- View all tickets for the FCM queue using this [ICM query](https://portal.microsofticm.com/imp/v3/incidents/search/advanced?sl=2gmgyntppxt).
- Do not wait for the DRI to engage a ticket that is related to a deployment in execution. Take initiative and mitigate the degrading deployment in addition to mitigating/resolving the ICM ticket. 

#### DRI Engagement

- **All deployments must be reviewed and approved by the DRI**. Any deployment that does not have their blessing will not get deployed.
- It is not the responsibility of the DRI to monitor deployments; take ownership of the code you're deploying and ensure it is successfully deployed to the last region.