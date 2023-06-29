# Change Guard User Guide
## Background
[Change Guard](https://aka.ms/changeguard) was developed to provide a standard interface to deployment systems to check if it is safe to proceed with the deployments. The primary focus is to provide a seamless integration with all deployment systems and evaluators, evaluator coordination, and exception management.

Today Azure does not have a centralized exception management workflow for handling deployment exception requests during Hi-Pri [Critical Change Only Advisories](https://microsoft.sharepoint.com/teams/AzureHighPriorityEventsProgramPortal/SitePages/Azure-Critical-Change-Only-Advisory.aspx) (CCOA). To centralize the exception management workflow and deliver a consistent customer experience, Federated Change Management (FCM), Express v2 (Ev2) and Hi-Pri Events teams have partnered to build Change Guard as an automated E2E solution for creating and managing Ev2 exception requests during CCOAs. 

### Critical Change Only Advisories (CCOA)
[Critical Change Only Advisories](https://microsoft.sharepoint.com/teams/AzureHighPriorityEventsProgramPortal/SitePages/Azure-Critical-Change-Only-Advisory.aspx) (CCOA) are a pre-defined period where engineering teams operate under a mandate allowing only critical changes to production. CCOAs applies to ring 0-2 services and production services including Networking, Compute, Storage, SQL Database, etc. No change should occur, except mandatory critical updates, as determined by respective organizations. CCOAs are planned 8 months in advance and are communicated in Fundamentals, PLR, and the weekly Hi-Pri Events Awareness email - join azhipricomms@microsoft.com.

To find out more about CCOAs, please visit https://aka.ms/ccoa. You will also find more information on your organization’s exception info and delegates, safe change guidance, and CCOA dates for this calendar year. Refer to [CCOA exceptions](http://aka.ms/ccoa/exceptions) for general guidance on how your organization is restricting change during this period.

## Best Practices

Service owners and approvers can make use of this end to end solution to plan and manage their exception requests during Hi-Pri CCOA for the following two scenarios:
- Proactive Scenario: Request/Approve exception before Hi-Pri CCOA
- Reactive Scenario: Request/Approve exception request during Hi-Pri CCOA

Want to make changes to the approvers list? Ask your Chief of Staff to do the following:
1.	https://aka.ms/serviceTree > Organization Tab
2.	Select your Service Group on Left panel
3.	Select Metadata
4.	Review/Edit Critical Change Approvers //Any new changes will use this updated list of approvers.

Note to Critical Change Approvers: 
- While reviewing exceptions during the below CCOAs, please take into consideration if the deployment affects AirGap cloud, as this will require cleared DRIs to travel into the physical environment.  
- Email may not be mobile friendly – so please use your Surface.
- The AzDeployer and APStager exception process remains unchanged.

## Feedback or Questions?
For Change Guard questions: [chgguardsupport@microsoft.com](mailto:chgguardsupport@microsoft.com?subject=Change%20Guard%20Help:%20[Team%20Name])

For Ev2-related questions: [Ask Ev2](mailto:ev2sup@microsoft.com?subject=Ev2%20Assistance:%20[Team%20Name]) 

For CCOA questions: [Azure Hi-Pri Event V-Team Core PM](mailto:ccoahelp@microsoft.com?subject=CCOA%20Assistance:%20[Team%20Name]) 

<!--For technical questions related to Hi-Pri events: [Azure Event Readiness System v-Team](mailto:eventreadiness@microsoft.com?subject=Hi-Pri%20Assistance:%20[Team%20Name]) -->