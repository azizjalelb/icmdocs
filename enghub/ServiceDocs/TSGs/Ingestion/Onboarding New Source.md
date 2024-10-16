## Onboarding a new source to the Change Insights

This is a developer guide to be used when onboarding a new source to Change Insights. We ingest most of our data from various source systems using KO Jobs. In the near future, we will be moving away from KO and move to ADF pipelines. 

Here are some steps which can help you onboard the new source quickly

1. Identify the Source cluster and get the access to the cluster
    1. Individual Access - Individual access to yourself so that you can analyze the data and test your ingestion queries
    2. Security Group Access - If the source team is willing to provide the access at the group level, please raise the access request to these two groups - 
    3. KO App ID Access - As we use KO to ingest the data into our Kusto, it is better to raise the access request as early as possible in the process. Our KO App Details: App ID - 3448865d-0a33-45b8-99ce-762f1f7d7caa, Tenant - 33e01921-4d64-4f8c-a055-5bdaffd5e33d

2. Analyze the Source data and map it to EntityModel Schema
    1. When we ingest data, we have to map the source data to [Entity Model Schema](https://microsoft.sharepoint.com/:w:/r/teams/SilverstoneProject/_layouts/15/Doc.aspx?sourcedoc=%7B4FE7A0EA-0EE7-486D-B535-C1A20BCB72AF%7D&file=EntityModel_Schema.docx&action=default&mobileredirect=true&share=IQHqoOdP5w5tSLU1waILy3KvAfldAnpC4vD89qwyIiqswnQ). 
    2. Entity Model Schema is the schema we use for 'EntityChangeEvents' table and we have to ingest the data into this table.

3. Few Tips when ingesting data
4. Create the KO Job in PPE
    1. Here is 
    2. Ko Job Documentation - 
    2. Sample Jobs in PPE
4. Testing the ingested data
5. Create Alarms and Metrics
    1. Change Count Monitor
    2. Latency Monitor
    2. Sample Monitors
        1. 
        2. 
6. Creating the MDM document when pushing the change into PROD
    1. 
    2. Sample MDM Documents
7. Deploying to Production
    1. 
    2. Sample KO Jobs in Production
