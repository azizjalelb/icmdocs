# Common Issues During CCOA Events

## Table of Contents

- [Overview](#overview)
- [Common Issues](#common-issues)
    1. [Duplicate Exception / Wrong Information in Exception](#1-wrong-information-in-exception)
    2. [Urgent Approval Needed](#2-urgent-approval-needed)
    3. [Onboarding to SafeFly Approval Process](#3-onboarding-to-safefly-approval-process)
    4. [Blocking Deployments to Test Subscriptions](#4-blocking-deployments-to-test-subscriptions)
    5. [Notification Email Not Working](#5-notification-email-not-working)

## Overview

This document serves as a cheatsheet for common issues that have surfaced during CCOA events. 
As we encounter new issues, we should add them to the list along with their solutions.

## Common Issues

### 1. Duplicate Exception / Wrong Information in Exception

Customers have created an exception with the wrong information and cannot create another exception while the old one is in place.

**Solution:**
Change Guard doesn’t support duplicate exceptions; to create a new one, the old one needs to be removed. 
This can only be done by the DRI, straight from the SQL Database.

Follow the TSG: [Archive Exception Request](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/archiveexceptionrequest)

> **Note:** You will need approval from the person who created the old exception (or their manager) before deleting it.

### 2. Urgent Approval Needed

Customers need an urgent approval and cannot wait for VP/CVP one.
This happens either due to security reasons or the VP/CVP not being available.

**Solution:**
Change Guard supports whitelisting at either the subscription or the build level. 
This can be done by the DRI, straight from the SQL Database.

Follow the TSGs:
- [Subscription Level Whitelisting](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/whitelistsubscription)
- [Build Level Whitelisting](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/whitelistbuild)

> **Note:** For this bypass, you will need approval from a principal level engineer/manager from the team asking for it.

### 3. Onboarding to SafeFly Approval Process
Customers need to onboard to the SafeFly approval process (instead of the default Change Guard one) or the other way around.
Change Guard supports two types of approval processes: one through the Change Guard portal and one through the SafeFly R2D approval.

**Solution:**
There is a list in the SQL DB whitelisting services that use the SafeFly approval process.

Follow the TSG: [Change Approval Process for Service](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/changeapprovalprocessforservice)

### 4. Blocking Deployments to Test Subscriptions
Customers ask why is Ev2/Change Guard blocking their deployment to Test subscriptions or to Canary regions.
During CCOA, Change Guard will block all deployments targeting PROD subscriptions and regions under CCOA scope.

**Solution:**
The subscription information is taken from Service Tree, where each customer marks their subscriptions as either Non-Prod or Prod.

More info in this TSG: [Ev2 Blocking Test Deployments](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/ev2blockingtestdeployments)

### 5. Notification Email Not Working
The notification email for a Change Guard exception request is not working.
We use two logic apps to send emails related to the approval process to the CVP/VP and the person who created the request.

**Solution:**
To investigate the email workflows, follow the TSG: [Changes to Non-Person Accounts](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/tsgs/changeguard/changestononpersonaccounts)
