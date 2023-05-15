

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