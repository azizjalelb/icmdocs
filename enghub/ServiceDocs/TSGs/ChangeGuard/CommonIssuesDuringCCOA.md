# Common issues that have surfaced during CCOA events

## Overview

This should act as a cheatsheet for common issues that have surfaced during CCOA events.
As we encounter new issues, we should add them to the list along with their solutions.

## Common issues

1. [Customers have created an exception with the wrong information and cannot create another exception while the old one is in place](#1-customers-have-created-an-exception-with-the-wrong-information-and-cannot-create-another-exception-while-the-old-one-is-in-place)
2. [Customers need an urgent approval and cannot wait for VP/CVP one](#2-customers-need-an-urgent-approval-and-cannot-wait-for-vpcvp-one)
3. [Customers need to onboard to the SafeFly approval process (instead of the default Change Guard one) or the other way around](#3-customers-need-to-onboard-to-the-safefly-approval-process-instead-of-the-default-change-guard-one-or-the-other-way-around)
4. [Customers ask why is Ev2/Change Guard blocking their deployment to Test subscriptions or to Canary regions](#4-customers-ask-why-is-ev2change-guard-blocking-their-deployment-to-test-subscriptions-or-to-canary-regions)
5. [The notification email for a Change Guard exception request is not working](#5-the-notification-email-for-a-change-guard-exception-request-is-not-working)

## 1. Customers have created an exception with the wrong information and cannot create another exception while the old one is in place

Customers have created an exception with the wrong information and cannot create another exception while the old one is in place.

### Solution:
Change Guard doesn’t support duplicate exceptions; to be able to create a new one, the old one needs to be removed.

This can only be done by the DRI, straight from the SQL Database.

To do this, follow the TSG: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/archiveexceptionrequest

> [!NOTE]: You will need approval from the person who created the old exception (or their manager) before deleting it.

## 2. Customers need an urgent approval and cannot wait for VP/CVP one

This happens either due to security reasons or the VP/CVP not being available.

### Solution:

Change Guard supports whitelisting at either the subscription or the build level.

This can be done by the DRI, straight from the SQL Database.

To do this, follow the TSGs:
-	Subscription level whitelisting: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/whitelistsubscription
-	Build level whitelisting: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/whitelistbuild

> [!NOTE]: For this bypass you will need approval from a principal level engineer/manager from the team asking for it.

## 3. Customers need to onboard to the SafeFly approval process (instead of the default Change Guard one) or the other way around

Change Guard supports two types of approval processes, one going through the Change Guard portal and one going through the SafeFly R2D approval.

### Solution:
There is a list in the SQL DB whitelisting services that use the SafeFly approval process.

To update the list, follow the TSG: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/changeapprovalprocessforservice

## 4. Customers ask why is Ev2/Change Guard blocking their deployment to Test subscriptions or to Canary regions

During CCOA, Change Guard will block all deployments that are targeting PROD subscriptions and regions under CCOA scope.

### Solution:
The subscription information we take from Service Tree, where each customer is marking their subscriptions as either Non-Prod or Prod.
More info in this TSG: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/ev2blockingtestdeployments

## 5. The notification email for a Change Guard exception request is not working

We use two logic apps to send emails related to the approval process to the CVP/VP and the person who created the request.

### Solution:
To investigate the email workflows, follow the TSG: https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/changestononpersonaccounts











Same resolve as [Changes in ServiceTree don't appear in Change Guard](ChangesServiceTreeDontReflectInChangeGuard.md).



Any changes done in ServiceTree are replicated to Change Guard using the Job [ChangeGuard Update Services Information](https://lens.msftcloudes.com/#/jobs/list?_g=(selectedJob:f581a6f8bf7c4b76b2267189f3cdc4ff,ws:cee2f53f-2d2a-40b4-a0c7-a33918652522)).

The job runs every 4h, that being the maximum delay until the changes are reflected.

> [!NOTE]
> Make sure the job is Healthy and Enabled.