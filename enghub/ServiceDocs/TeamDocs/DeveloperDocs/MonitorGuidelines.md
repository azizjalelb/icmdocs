# Guidelines to Create Monitors

There are two monitoring systems which we use extensively in our team. 
1. Monitors Created through Jarvis
2. Monitors Created through Application Insights


Here are the few best practices/guidelines to be considered when creating a monitor:
1. Determine what you intend to achieve with the new monitor. It can be measuring the performance(eg:latency), uptime(zero counts),  error rates, etc.
2. Based on the objective of the monitor, determine the key components that need monitoring. It can be an api/server, ko/lens job failure, database performance, etc.
3. Not all the components need monitoring, prioritize based on the criticality. For eg; a 5XX error should be prioritized over 4XX errors for the severity of the alarm.
4. Identify the metrics which will provide the insight into the health, performance, etc. of the components. Common metrics we have used for ingestion are latency, count. For API, we are focusing on the 5XX errors, 4XX errors.
5. Key thing while setting up an alarm is to understand the baseline. Understand the baseline of the system as part of the load testing.
6. Define the thresholds based on the baselines observed in step#5. 
7. Configure alerts in the tiered levels, that is Sev-2 for Critical Severity, Sev-3 for warning, etc. Threshold defined in Step#6 should be used as a guideline for setting up the severity.
8. Check the integration with the ICM tool. Make sure PROD and PPE classification is done correctly and the email messages reflect the right environment name.
9. Test the Monitors and ensure they are triggered at the right baseline.
10. Once the monitor is enabled in the PPE/PROD, keep it in silent state for a day or two and monitor the monitor. That is check how the expressions are being evaluated.
11. After a day or two of monitoring the monitor, enable the monitor and monitor it daily for few days to ensure the thresholds are good.
12. As the system matures, periodically update the monitor to align with new changes, new load and update the threshold baselines.

    #### Examples of the monitors we have in production
    1. [Latency Monitor for Express V2 Ingestion](https://portal.microsoftgeneva.com/manage/monitors/monitor?activity=edit-monitor&version=1&action=3&account=fcmmdsprodaccount&monitorId=0d22541a-8b3f-4928-80c6-19d3317fcd24)
    2. [Monitor for KO Job Failures](https://portal.microsoftgeneva.com/manage/monitors/monitor?activity=edit-monitor&version=1&action=3&account=fcmmdsprodaccount&monitorId=d21bfc1f-a5e0-4fc0-b1a6-ce85e7860e06&hideLeftNav=true&newManageSessionId=bb0564ea-1eab-47dc-8338-eec9c3930fea)
    3. [Monitor for AKS Change Count](https://portal.microsoftgeneva.com/manage/monitors/monitor?activity=edit-monitor&version=1&action=3&account=fcmmdsprodaccount&monitorId=286e6034-6ce9-47bc-a1a0-4de561178082&hideLeftNav=true&newManageSessionId=bb0564ea-1eab-47dc-8338-eec9c3930fea)
    4. [Monitor for API 5XX Errors](https://ms.portal.azure.com/#@MSAzureCloud.onmicrosoft.com/resource/subscriptions/8830ba56-a476-4d01-b6ac-d3ee790383dc/resourceGroups/ChangeExplorerV2WestUS/providers/microsoft.insights/scheduledqueryrules/%5BPROD%5D%5BWest%20Us%5D%20CSS%20GetChangesAsync%20API%20-%205xx%20ResultCode/overview) : Get JIT for the subscription#8830ba56-a476-4d01-b6ac-d3ee790383dc and use the SAW Machine to access this link. 