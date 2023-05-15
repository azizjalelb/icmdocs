# EV2 blocking Non-Production/Test deployments during CCOA events

## Overview

Same resolve as [Changes in ServiceTree don't appear in Change Guard](ChangesServiceTreeDontReflectInChangeGuard.md).

When EV2 checks with Change Guard for a deployment, Change Guard also checks if the Subscription is defined in ServiceTree as Production or Non-Production.

If the subscription is Non-Production, the deployment can continue.

There are times when a subscription is initially set up as Production and later on changed to Non-Production; this could lead to a difference between ServiceTree and

Change Guard until the job that syncs the changes will run again (the job runs every 4h). After a new job run, the subscription metadata will be synced and show the latest values

from ServiceTree, allowing the Non-Production EV2 deployments to continue.

## Solution

Any changes done in ServiceTree are replicated to Change Guard using the Job [ChangeGuard Update Services Information](https://lens.msftcloudes.com/#/jobs/list?_g=(selectedJob:f581a6f8bf7c4b76b2267189f3cdc4ff,ws:cee2f53f-2d2a-40b4-a0c7-a33918652522)).

The job runs every 4h, that being the maximum delay until the changes are reflected.

> [!NOTE]
> Make sure the job is Healthy and Enabled.