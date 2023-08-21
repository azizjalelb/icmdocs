# [FCM-MCM][ChangeExplorerV2] Support for `Search By Incident Id`

## Change Summary

Change Owner   | Andres Rojas Sanchez (andresro@)
-------        | ------
Pull Requeset   | [Deploying IIP, LIP and UBS for SearchByIncidentId](https://msazure.visualstudio.com/One/_git/FCM-ChangeExplorer-Backend/pullrequest/7322666)
Work Item | [Search by IncidentId](https://msazure.visualstudio.com/One/_sprints/backlog/FCM/One/Zinc/CY22Q4/2Wk/2Wk6?workitem=14995813)
Start Time | 12-12-2022T16:00
End Time |  12-12-2022T18:00
Status | Pre-Deployment

> **What is the purpose of this change?**  These deployments are to support SearchingByIncidentId (see the work item above).

> **What is being changed?** The following will be changed:
>
> - IncidentInformationProvider (IIP) - Adding `GET GetIncidentInformationAsync` endpoint
> - LocationInformationProvider (LIP) - Adding `POST GetMultipleLocationDetailsAsync` endpoint
> - UIBackendService (UBS) - Adding `POST SearchByAsync` endpoint

## Risk Assesment

> **What are the risks of this change?** Deploying this change can cause availability and latency increases in the components that are being deployed (IIP, LIP and UBS). Additionally, if the components are not configured correctly in the EV2 templates we might receive availability issues stemming from misconfigured storage accounts, key vaults or certificates.

> **What is the worst case scenario?** Worst case scenario is an availability outage in one of the components that causes our customers to experience availability dips. Since all three components are vital for the operation of ChangeExplorerV2, any single component outage will impact the service.

> **How are the risks mitigated?** The risks are mitigated by:
>
> - Conduncting pre-validation steps in INT to ensure behavior as expected.
> - Testing rollback steps prior to edeployment in case an issue arises and rollback is required.
> - Deploying a single component at a time via ADO/EV2 and ensuring it is successfully updated in the respective environment.
> - Testing a component's individual endpoints to ensure no impact on existing service.

> **How will you detect a problem cause by this change?** We will manually verify the update by
>
> - Hitting the new endpoints with postman and ensuring that they work as expected.
> - Executing the manual test cases as defined in [ChangeExplorerUI Manual Test Cases](https://microsoft-my.sharepoint.com/:x:/p/andresro/EY7X2UYx0RBFl1CtcerTJN0BQkBaHtk0VK0F2vulTQDxbg?e=8FCKp8)
> - Checkeing the availability and latency alarms configured in the environmenet in addition to checking ICM tickets cut to the DRI.

## Rollback Steps

> [!CAUTION]
> Validate that these rollback steps are working in INT prior to .AME deployments

> **What are the rollback steps?** The rollback steps are:
>
> - For Azure Function, we will swap staging to revert back to the older state.
> - For App Service, we will swap staging to revert back to the older state.

## Pre-Validation Steps

### Postman Steps

After deploying the code to INT, validate the following using postman. Download the [ChangeExplorerV2 Postman Collection](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Forms/AllItems.aspx?viewpath=%2Fteams%2FWAG%2FEngSys%2FServiceMgmt%2FChangeMgmt%2FShared%20Documents%2FForms%2FAllItems%2Easpx&id=%2Fteams%2FWAG%2FEngSys%2FServiceMgmt%2FChangeMgmt%2FShared%20Documents%2FChangeExplorerV2%2FPostman&viewid=9f970ef2%2Dbecc%2D4c74%2Da8b2%2D2c4534e1be58&view=0&OR=Teams%2DHL&CT=1669670235563&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMjExMTQxMjgwMCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D) if you haven't already.

- Validate `GET GetIncidentInformationAsync`
- Validate `POST GetMultipleLocationDetailsAsync`
    - Validate this with multiple valid locations, single valid location and no valid locations.
- Validate `POST SearchByAsync`
    - Validate this with filter panel and incidentId types to ensure expected behavior.

### ChangeExplorerV2UI Manual Test Case Steps

Execute all of the manual test cases as defined in [ChangeExplorerUI Manual Test Cases](https://microsoft-my.sharepoint.com/:x:/p/andresro/EY7X2UYx0RBFl1CtcerTJN0BQkBaHtk0VK0F2vulTQDxbg?e=8FCKp8)

## Change Execution Steps

> [!CAUTION]
> Only execute these steps if pre-validation was successful. Otherwise, abort the change and investigate the issues in pre-validation.

Execute the following steps:

### PPE

- Create a PR that merges the changes in the `develop` branch into `main` (`main` is our target branch for PPE and PROD).
- Get an approval and merge changes into `main`.
- After merge, the release pipeline will automatically build and generate a release. This release will require an approval from SAW machine. Get an approval from a team member.
- Wait for the release to finish.
- (For IIP) IIP is a new component that is not hooked up to existing resources in PPE and Prod. Ensure that
    - It has access to Kusto.
    - It has access to kevaults/secrets/certificates.
    - It is configured in APIM.
    - It is configured in frontdoor if required.
- Validate each of the components and their newly added endpoints via postman:
    - Validate `GET GetIncidentInformationAsync`
    - Validate `POST GetMultipleLocationDetailsAsync`
        - Validate this with multiple valid locations, single valid location and no valid locations.
    - Validate `POST SearchByAsync`
        - Validate this with filter panel and incidentId types to ensure expected behavior.
- Execute all the manual test cases as defined in Execute all of the manual test cases as defined in [ChangeExplorerUI Manual Test Cases](https://microsoft-my.sharepoint.com/:x:/p/andresro/EY7X2UYx0RBFl1CtcerTJN0BQkBaHtk0VK0F2vulTQDxbg?e=8FCKp8)

>[!NOTE]
> After PPE validation, complete the following:
> - Configure latency and availability metrics for each endpoint
    >   - Latency should be set to P90 of 5s for 3 data points of 5 minutes (i.e. 15 consecutive minutes of >= 5 second latency for P90 requests).
>   - Availability should be set to 1 data point of 4XX or 5XX of 5 minutes.
> - For each metric configured above (6 total, 3 availability/3 latency) configure an alarm that notifies the FCM DRI.
    >   - For each alarm, ensure that it is pointed to a relevant TSG in engineering hub with instructions on how to mitigate the issue.

### PROD

- This release will require an approval from SAW machine. Get an approval from a team member.
- Wait for the release to finish.
- (For IIP) IIP is a new component that is not hooked up to existing resources in PPE and Prod. Ensure that
    - It has access to Kusto.
    - It has access to kevaults/secrets/certificates.
    - It is configured in APIM.
    - It is configured in frontdoor if required.

## Post-Validation Steps

- Validate each of the components and their newly added endpoints via postman:
    - Validate `GET GetIncidentInformationAsync`
    - Validate `POST GetMultipleLocationDetailsAsync`
        - Validate this with multiple valid locations, single valid location and no valid locations.
    - Validate `POST SearchByAsync`
        - Validate this with filter panel and incidentId types to ensure expected behavior.
- Execute all the manual test cases as defined in Execute all of the manual test cases as defined in [ChangeExplorerUI Manual Test Cases](https://microsoft-my.sharepoint.com/:x:/p/andresro/EY7X2UYx0RBFl1CtcerTJN0BQkBaHtk0VK0F2vulTQDxbg?e=8FCKp8)

>[!NOTE]
> After Prod validation, complete the following:
> - Configure latency and availability metrics for each endpoint
    >   - Latency should be set to P90 of 5s for 3 data points of 5 minutes (i.e. 15 consecutive minutes of >= 5 second latency for P90 requests).
>   - Availability should be set to 1 data point of 4XX or 5XX of 5 minutes.
> - For each metric configured above (6 total, 3 availability/3 latency) configure an alarm that notifies the FCM DRI.
    >   - For each alarm, ensure that it is pointed to a relevant TSG in engineering hub with instructions on how to mitigate the issue.
>
## Additional Steps

Update this doc with notes/validations as you execute it.