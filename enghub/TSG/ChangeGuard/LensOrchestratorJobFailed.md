## Geneva Orchestrator job 'ChangeGuard Update Services Information' in project 'FCM' failed 

### The Job "ChangeGuard Update Services Information" can be found here:

* [ChangeGuard Update Services Information](https://lens.msftcloudes.com/#/jobs/list?_g=(selectedJob:f581a6f8bf7c4b76b2267189f3cdc4ff,ws:cee2f53f-2d2a-40b4-a0c7-a33918652522))
* The job updates several Kusto and SQL tables on all of the existing environments (INT/PPE/PROD).
* The jobs is scheduled to run every 4h and the duration averages around ~30-35 minutes per run.

### Solution:
* Make sure the job is **Healthy** and **Enabled**.
* The job has a linear retry mechanism, retrying up to 2 times after a delay of 10 minutes.
  - The retry process will take care of any transient failures.

**Note:** Non transient failures will need further investigation and are not part of this TSG.


 