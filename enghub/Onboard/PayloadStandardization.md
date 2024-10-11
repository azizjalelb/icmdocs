# Change Insights Payload Standardization

| Deployment Systems | Change Data Payload | Change Data Payload Cannonical (NorthStar) |
| --- | --- | --- |
| PilotFish (app) | **<servicename>=<buildlabel>** <br/><br/> *Example:* RdAgentUpdater=r_feb_2024_150_948_66_947  | PF/<VEName>/<ServiceName>=<SchemaVersion>/< ADOOrg>/< ADOProject>/<Repository>/<Branch>/<Version> |
| PilotFish (data) | **<datafolder>=<version>** <br/><br/> *Example:* configuration=5123646 | PF/<VEName>/<DataFolder>=<SchemaVersion>/<SourceIdentifier>/<ADOOrg>/<ADOProject>/<Repository>/<Branch>/<Version> or <SMB Foldername> or <SourceDepotpath>/<Version>|
| ExpressV2 | **<ServiceTreeId>/<ServiceGroupName>=<Version>** <br/><br/> *Example:* 3b47be62-c17d-4be1-b473-8f83de433718/ConfigDeploy.ServiceGroup=1.0.117.2655 (git_ad_commoncontent_master) | EV2/<ServiceTreeId>/<ServiceGroupName>=: <SchemaVersion>/<ADOOrg>/<ADOProject>/<Repository>/<Branch>/<Version> |
| AzDeployer (v1/v2) | **<component>=<template>;<branch>;<version>** <br/><br/> *Example*: SLB=UpdateRingFlow.xml;git_networking_slb_hotfix_0_13_1321_0;0.13.1321.13 | <ComponentName>/<Template>=<SchemaVersion>/<ADOOrg>/<ADOProject>/<Repository>/<Branch>/<Version>|


