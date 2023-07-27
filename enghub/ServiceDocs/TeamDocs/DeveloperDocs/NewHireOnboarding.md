# FCM - New Hire Onboarding

[Work In Progress]

**Welcome to Microsoft!**

## Equipment Setup

1. To gain access to the production systems you need to request a SAW machine and YubiKeys.
    1. Request for SAW machine by reaching out to your business admin. This is the same person who has connected with you regarding your Microsoft equipment and devices. The device takes around 2 weeks to get delivered home (during Covid-19 WFH policy) so please follow [these](https://strikecommunity.azurewebsites.net/articles/1069/ame-account-creation-and-yubikey-request.html) steps to request creation of an AME account on your behalf with Naveen as the approver. This account can be created/requested only with AME credentials so someone from the team will create one for you and the manager will then approve their request [here](https://aka.ms/OneIdentityApprovals).
    2. Request for a YubiKey ([here](https://microsoft.sharepoint.com/teams/cdocidm)). This is required to gain access to the production systems and to get credentials for some local development environments of the team. Follow [these](https://microsoft.sharepoint.com/teams/CDOCIDM/SitePages/YubiKey-Management.aspx) steps to setup your YubiKey once the AME account has been approved.
    3. Follow these steps to set up your SAW machine ([here](https://microsoft.sharepoint.com/sites/Security_Tools_Services/SitePages/SAS/SAW-Re-Image-or-New-OS-Install-Guide.aspx)). More details about SAW can be found here for curious folks.
2. If you have received two MS devices - a laptop and a desktop. We recommend to setup the desktop first as most likely that is a more powerful machine. You can always use laptop + RDP to connect to your desktop and start development.

## New to FCM

Welcome to the Federated Change Management (FCM) team!

FCM provides actionable insights derived from Service State and Change across Microsoft cloud, service layers and dependencies. By federating, correlating and merging data from these sources, FCM can derive and expose actionable insights to help engineers make better informed decisions. By doing so FCM analytical insights can reduce the risks to current production environments and reduce the time to mitigate live site incidents.

Useful links related to our team:

1. Backlog Issues in ADO ([h](https://msazure.visualstudio.com/Service360/_backlogs/backlog/FCM/Stories)<span style="text-decoration:underline">ere</span>)
1. Security & Vulnerability Dashboard ([S360](https://vnext.s360.msftcloudes.com/blades/allup))
1. Incidents for FCM team ([here](https://portal.microsofticm.com/imp/v3/incidents/search/advanced)) [<span style="text-decoration:underline">Shared Queries&gt;Federated Change Management&gt;Default&gt;All FCM Active</span>]

### Required Permissions

1. Request permissions for "FCM Feature Crew" [here](https://idweb.microsoft.com/identitymanagement/aspx/groups/AllGroups.aspx). This will get you access to repos and ADO
1. Request permissions to view team incidents from any Admin of the FCM Team ([here](https://portal.microsofticm.com/imp/v3/administration/teamdashboard/details?id=62952))
1. Request permission to get added to the FCMINTKV Key Vault ([here](https://ms.portal.azure.com/#@microsoft.onmicrosoft.com/resource/subscriptions/e1573d42-0032-4eb9-a4e3-2f7a429afb81/resourceGroups/fcmmdspipeint/providers/Microsoft.KeyVault/vaults/FCMINTKV/overview))
1. Request to get added into the FCM team to view sprints and tasks ([here](https://msazure.visualstudio.com/Service360/_settings/teams?teamId=3f9bd753-74ba-474e-9271-3786f05e65f3))
1. Request necessary permissions [*create branch, create tag, contribute*] for the repositories ([here](https://msazure.visualstudio.com/DefaultCollection/One/_settings/repositories?repo=c0940bb2-a3bc-4b7e-855b-f2728e9bf350&amp;_a=permissionsMid)) from Naveen
1. Request access to "WA Analytics Team" MyAccess group from [here](https://myaccess/identityiq/accessRequest/accessRequest.jsf#/accessRequestSelf/add)
1. Request access to FCM Incidents

### Basic Setup

1. Install Azure CLI on Windows ([instructions](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli))
1. Install PowerShell 7.2 LTS on Windows ([instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2))
1. Install SQL Server Management Studio ([instructions](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15))
1. Install the latest version of Visual Studio Enterprise 2019 ([instructions](https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes))
1. Install Git for Windows ([here](https://git-scm.com/download/win))
1. Verify that Hyper-V is enabled ([instructions](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)) and then install Docker for Windows ([here](https://docs.docker.com/desktop/windows/install/)). The docker installation will provide an option to install WSL 2, please select this installation.
1. Install the latest version of Visual Studio Code from MS Store. Though the team uses VS (as installed in Step #4) but this is a nice tool to have for terminal requirements.
    
## FCM Products

### Change Card

### Change Guard

It used to be known as Change Manager once.

Below are the useful links to better understand and locally develop this product:

- More resources ([here](bookmark://_Change_Guard))

### Change Explorer

It is designed to be a flexible tool for asking the question, "What's Changed?". You can specify some context (Service, Component, or Location) and a date range and Change Explorer will provide you with a list of changes meeting those criteria. It also displays several charts that breakdown the data by a variety of pivots and lets you filter the data table by clicking segments of the charts.

Below are the useful links to better understand and locally develop this product:

- Code Repository ([here](https://msazure.visualstudio.com/DefaultCollection/One/_git/EngSys-ChangeManagement-FCM))
- Metrics & Alarm Dashboard *TODO*
- Backlog Items *TODO: Define a tag that can be assigned to its stories and mention it here*
- More resources ([here](bookmark://_Change_Explorer))

### FCM Development Practices

#### Infra Pipeline Configuration
*TODO: Define the environments that are used and their purpose*

#### Local Development
Please follow each repository's readme file for local workspace setup.

#### Pipeline Deployment
*TODO: Define the precautions and practices to be followed when deploying any software on a high level. The details of each service should be present in respective readme files.*

### Operational Excellence

#### DRI
*TODO: Define the responsibilities of the DRI and the dashboards that must be presented in the meeting*

#### Team KPI(s)

This section provides high level concise view of the key API(s) for our team. The table below highlights the clients that call our services and the dependencies that our services have along with their use cases. There are also details about the SLA and throughput information for clients for quick reference during an incident.

Dashboards:

*Mention the links to main monitoring dashboard*

| S. No. | Product | API | Description | Clients | Dependency | Details |
| --- | --- | --- | --- | --- | --- | --- |
| 1. |  |  |  |  |  |  |
| 2. |  |  |  |  |  |  |
| 3. |  |  |  |  |  |  |

#### Dependency Use-cases

#### Client Use-cases

### FCM Acronyms

These are the commonly used acronyms within the FCM team in Microsoft ecosystem.

| **TLA**  | **Description** |
|-----------|------------------|
| AAD      | Azure Active Directory |
| ADO      | Azure Dev Ops |
| ARM      | Azure Resource Manager |
| CLI      | Command Line Interface |
| DRI      | Designated Responsible Individual |
| ICM      | Incident Manager |
| IIS      | Internet Information Server |
| JIT      | Just In Time |
| KPI      | Key Performance Indicator |
| SAW      | Secure Admin Workstation |
| TLA      | Three Letter Acronym |
| TSG      | Troubleshooting Guide |
| WSL      | Windows Subsystem for Linux |
| RDP      | Remote Desktop Protocol |

### Contact Us

#### Further Reading
    
**Authorization & Authentication in MS**

- You would have heard terms like YubiKey, SmartCard & SAW machines. All these things are used for authentication within Microsoft Azure. Our PPE and PROD machines run in AME domain whereas our local machines run in NORTHAMERICA domain (can be Redmond, Hyderabad, etc.). In order to connect to the AME domain, YubiKey(s) and SmartCard(s) are used. SmartCard is an older way of authentication and was replaced by YubiKey. SAW machines are laptops which are configured in AME domain, so they don't require extra authentication to connect. They have restricted network access. These machines are used to get JIT access.
- There are two types of subscriptions (term for logical grouping of cloud resources) - Prod and Non-Prod. Non-Prod subscriptions provide persistent authentication, meaning we can whitelist our user in these subscriptions and can then use our local machines along with YubiKey/SmartCard to connect. Whereas PROD subscriptions require Just-In-Time (JIT) authentication. JIT access is a process where our user is whitelisted on a particular PRODUCTION subscription upon placing an approval-request via portal. This whitelisting is short lived and while it is present, we can either use SAW machine or local machine + extra authentication to connect to PROD systems.

#### Change Card
- Team discussion video to understand Change Card accuracy calculation & DRI assistance ([here](https://msit.microsoftstream.com/video/0927a4ff-0400-b564-63d4-f1eb6d8f3079))

#### Change Guard
- Detailed video explanation as to why this product is needed ([here](https://msit.microsoftstream.com/video/c749a1ff-0400-85a8-4ba5-f1eb7c52bb04))

#### Change Explorer
- User Journey Walkthrough ([here](https://pappdocs.msftcloudes.com/EngSys-CloudES-UserDocs/GenevaAnalyticsDocs/FCM/ChangeExplorer/ChangeExplorer.html))
- Brownbag video highlighting the production usage of Change Explorer ([here](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Videos/FCM%20Brownbag%20for%20Cloudnet%20Incident%20Ma.%20.%20.%20-%20Wednesday,%20July%2026,%202017%2012.09.49%20PM.mp4?csf=1&amp;e=q4VKiD&amp;cid=6962cc77-ddb2-47d4-b297-7a46bab63ced))
- Local development setup ([here](https://microsoft.sharepoint.com/teams/FCMEngineering/_layouts/15/Doc.aspx)) [to be deprecated and instructions to be moved to repo's ReadMe]
    
#### Remote Desktop Connection

Follow the instructions mentioned [here](https://www.bing.com/search?q=how%20to%20use%20remote%20desktop%20to%20connect%20to%20a%20windows%2010%20pc%20site:microsoft.com&amp;form=B00032&amp;ocid=SettingsHAQ-BingIA&amp;mkt=en-US&amp;shtp=Email&amp;shid=4da7fe7e-b124-4b4a-ad24-b0432bc50429&amp;shtk=SGVscCBmcm9tIE1pY3Jvc29mdCA%3D&amp;shdk=R2V0IGhlbHAgYWJvdXQgeW91ciBNaWNyb3NvZnQgcHJvZHVjdHMgb24gQmluZyA%3D&amp;shhk=%2B4C%2B5ZCLO4NQgGJmGeRLJNW9K31cCGY7TM%2BvLhSV0Qo%3D&amp;shtc=13) to configure RDP access to your desktop/laptop.

#### AVD Desktop
If you'd rather use a remote desktop rather than a physical desktop in office or at home, follow the steps outlined here: [AVD Developer Workstation (sharepoint.com).](https://microsoft.sharepoint.com/sites/Security_Tools_Services/SitePages/WindowsVirtualDesktop/WVD-Workstation.aspx) Note that this is a replacement of the physical desktop. Approval is required by manager.

Relevant info:
- 8 Digit Cost Center Code: 10229797
- Finance Lead email: jur@microsoft.com (Julian Johnson)

#### Troubleshooting
- AME cert not appearing as a login option ([here](https://microsoft.sharepoint.com/:w:/r/teams/Aznet/_layouts/15/Doc.aspx?sourcedoc=%7B013F5197-47B2-43C6-94F0-B61417798CA8%7D&amp;file=AME%20SC%20Certificate%20login%20issues.docx&amp;action=default&amp;mobileredirect=true&amp;DefaultItemOpen=1&amp;share=IQGXUT8BskfGQ5TwthQXeYyoAYj-WH2fOx-lB7wX2pjcLDA&amp;cid=f61b5081-09e9-4437-ac12-92c12ad26ba6))

#### Developer Links
- FCM Manual Change Management Template ([here](https://microsoft.sharepoint.com/:w:/t/FCMEngineering/EaiYm3rU_AxAoVnpqwOky3gBsukMACz2BwaW0EnNLUue4A?e=fmWK9M))
- Design Template (here)