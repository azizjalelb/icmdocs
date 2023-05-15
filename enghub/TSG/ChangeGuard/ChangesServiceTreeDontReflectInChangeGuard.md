# Changes in ServiceTree don't reflect in ChangeGuard

## Overview

Any changes done in ServiceTree are replicated to Change Guard using the Job [ChangeGuard Update Services Information](https://lens.msftcloudes.com/#/jobs/list?_g=(selectedJob:f581a6f8bf7c4b76b2267189f3cdc4ff,ws:cee2f53f-2d2a-40b4-a0c7-a33918652522)).

The job runs every 4h, that being the maximum delay until the changes are reflected.

> [!NOTE]
> Make sure the job is Healthy and Enabled.