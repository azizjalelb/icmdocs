## Onboarding a New Source to Change Insights via Ingestion (KO Job)

This guide is intended for developers onboarding a new source to Change Insights. We primarily ingest data from various source systems using KO Jobs. In the near future, we plan to transition to ADF pipelines.

### Steps for Onboarding a New Source

1. **Identify the Source Cluster and Obtain Access**
    - **Individual Access:** Ensure you have individual access to analyze data and test ingestion queries.
    - **Security Group Access:** If the source team allows group-level access, request access for the following groups:
    - **KO App ID Access:** Since we use KO to ingest data into Kusto, request access early in the process. KO App Details: 
        - App ID: `3448865d-0a33-45b8-99ce-762f1f7d7caa`
        - Tenant (AME): `33e01921-4d64-4f8c-a055-5bdaffd5e33d`

2. **Analyze Source Data and Map to EntityModel Schema**
    - Map the source data to the [Entity Model Schema](https://microsoft.sharepoint.com/:w:/r/teams/SilverstoneProject/_layouts/15/Doc.aspx?sourcedoc=%7B4FE7A0EA-0EE7-486D-B535-C1A20BCB72AF%7D&file=EntityModel_Schema.docx&action=default&mobileredirect=true&share=IQHqoOdP5w5tSLU1waILy3KvAfldAnpC4vD89qwyIiqswnQ). This schema is used for the `EntityChangeEvents` table.

3. **Create the KO Job in PPE**
    - Use KO Jobs to ingest data into Kusto. Refer to the [KO Documentation](https://eng.ms/docs/products/kusto/orchestrator).
    - Access our [KO Jobs in PPE](https://kustoorchestrator-prod-web.azurewebsites.net/Manage?cluster=Fcmdatappe.Westus2&database=EntityModel).

4. **Test the Ingested Data**
    - Create a testing document and place it in the [Testing Docs Folder](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Forms/AllItems.aspx?id=%2Fteams%2FWAG%2FEngSys%2FServiceMgmt%2FChangeMgmt%2FShared%20Documents%2FDesign%20Docs%2FChange%20Ingestion%2FTesting%20Docs&viewid=9f970ef2%2Dbecc%2D4c74%2Da8b2%2D2c4534e1be58).
    - Refer to sample testing documents:
        - [AzDM Testing Doc](https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/Doc.aspx?sourcedoc=%7BEE9AEBBD-C426-41E2-8EE2-2019D55EC5F1%7D&file=AzDM%20Change%20Ingestion%20Testing.docx&action=default&mobileredirect=true)
        - [Service Fabric Testing Doc](https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/Doc.aspx?sourcedoc=%7B9C288491-18BE-4035-90A3-E887753A2451%7D&file=ServiceFabric_Tenants_Validation.docx&action=default&mobileredirect=true)
    - Use the [Testing in PPE Dashboard](https://kusto.azure.com/dashboards/f6687c24-35db-4cfb-a7db-34a85bdc26ec?p-_startTime=2days&p-_endTime=now&p-_ppeSource=v-RequestProcess&p-_zeroCountTimePeriod=v-30m&p-_serviceNamePPE=all#050c8161-3c87-4a6e-9cf0-152a1fb57aee) for testing. This dashboard will eventually replace steps 1 and 2.

5. **Create Alarms and Metrics**
    - **Change Count Monitor:** Set up to alert when data ingestion fails for a given period, aiding in debugging source or pipeline issues.
    - **Latency Monitor:** Set up to track data reception within threshold latency times.
    - Sample Monitors:
        - [ChangeCount Monitors](https://portal.microsoftgeneva.com/manage/monitors?account=fcmmdsprodaccount&state=[[%22tags%22,%22%3D%3D%22,[%22EntityModel%22]],[%22_search%22,%22Change%20Count%22]]%20)
        - [Latency Monitors](https://portal.microsoftgeneva.com/manage/monitors?account=fcmmdsprodaccount&state=[[%22tags%22,%22%3D%3D%22,[%22EntityModel%22]],[%22_search%22,%22Latency%22]]%20)

6. **Create the MCM Document for Production Deployment**
    - Create an MCM document for any production deployments. It must be approved by the DRI before pushing any changes to production.
    - Refer to [Sample MCM Documents](https://microsoft.sharepoint.com/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Forms/AllItems.aspx?id=%2Fteams%2FWAG%2FEngSys%2FServiceMgmt%2FChangeMgmt%2FShared%20Documents%2FEngineering%20Excellence%2FMCMs%2F2024%2FOctober&viewid=9f970ef2%2Dbecc%2D4c74%2Da8b2%2D2c4534e1be58).

7. **Deploy to Production**
    - Once the MCM document is approved, deploy the functions into production and enable KO Jobs in PROD.
    - Access our [KO Jobs in PROD](https://kustoorchestrator-prod-web.azurewebsites.net/Manage?cluster=Fcmdata&database=EntityModel).

8. **Verify Changes in OneDeployFCM**
    - Verify the changes in [OneDeployFCM](aka.ms/onedeployfcm).

9. **Verify Changes in FCMAISummary**
    - Ensure all changes are reflected accurately in FCMAISummary, if applicable. Not all new ingestions will automatically reflect in FCMAISummary.