

# Mitigation steps for Lens Orchestrator Job Failures
1)  Go to ICM incident ticket and find the name of the Lens Orchestrator job that failed.

2) Go to Lens Explorer FCM Workspace

3) Click on the job that failed.

4) From the panel that opened at the bottom, find the last failed instance of the job and click on the options icon (three vertical dots) at the end of the row and click on "View Execution Logs"

5) Read the "Exception Message" on the new page.

6) If the error message is related to Kusto such as: "Kusto client failed to send a request to the service: 'The underlying connection was closed: A connection that was expected to be kept alive was closed by the server.'"
    * Check if the cluster('fcmdata.kusto.windows.net').database('FCMKustoStore') is up and running or not.
        * If there is an issue with the Kusto cluster, investigate the issue and/or create a Sev2 incident on Kusto team to get help.
        * If the Kusto cluster and the database is up and running, rerun the job. It's most likely a temporary connection failure to the Kusto cluster.

7) If the error message is a semantic error, copy the query that cause the failure in the process to your Kusto Explorer and try running.
    * If it fails, 
        * debug the issue
        * fix it 
        * update the query in the process in Lens oOchestrator job 
        * Re-run the job
    * If it succeeds,
        * check the execution logs to make sure that you do not have an extra ';' at the end of the query which is causing the process to fail.
        * rerun the job.
     

8) If the error is realated to Azure Key Vault, 
    * Try rerunning the job.
        * If it fails, reach out to the AKV team.


9) If the issue is none of the above, act based upon the execution logs and if you beieve the issue is not on our end, reach out to the team which owns the product that is causing the failure or reach out the Lens Orchestrator team.


# Special Steps for:
### FCM_ChangeExplorerV2_PopulateSimplifiedNetworkTopology_Prod
1. This lens job creates a backup table by pulling in the data by using various kusto function.
    Once this backup table is fully created, it runs a kusto function to perform validations by comparing new data v/s old data.
2. To find names of the ingestion function, validation function and backup table please refer to the [lens explorer job](https://lens.msftcloudes.com/#/job/12fe54c24f4b4e7cb07d5ab35fe580d3?_g=(ws:'cee2f53f-2d2a-40b4-a0c7-a33918652522')).
3. Read the exception message, if it has a semantic error with `assert() has failed with message` it would mean that validation assertions have failed.
4. Run the validation function(s) on ADX (Azure Data Explorer) to see which exception is failing.
5. You can now slice and dice the queries to find the exact root cause.
6. We need to connect with ARG team (agsupport@microsoft.com) if:
    * the count difference is 5% above threshold
    * there is zero count of any location type
7. Involve other members of the FCM team if:
    * multiple parents are detected
    * the count difference is (1-5)% below threshold 
