# Overview 

This program was created to assist the ACE DRIs in correctly assigning ICM tickets to the responsible team with the goal to reduce the number of ICMs incorrectly assigned to the OneDeploy team. Historically, when a DRI is unable to pinpoint the responsible team for an ICM, it would get assigned to OneDeploy which resulted in an influx of tickets that the OneDeploy team would initially be involved in until the appropriate team was determined. This would take up the time of the OneDeploy team when it could be better utilized for incidents that they are actually responsible for. Our goal is to change that through case studies, tool improvements, playbooks, and trainings which in the end, will reduce the TTM for ICM incidents. This program is continuously working to improve this area thus, this wiki site will be frequently updated with new scenarios, tooling education, and other information so keep checking back.

## What We have Done so Far

In order to get a information for how ACE DRIs assign DRIs, we conducted a set of usability tests. These tests consisted of coming up with three scenarios, which are referenced in the Scenarios Section, and having them walk through the way they would approach them. We found that there are many different ways to come to the correct solution and there were some that were not able to come to a solution. 

This determined a few things, one being that some approaches were quicker than others. With this in mind, we added the scenarios to this wiki that shows the best path to take and the preferred tools to use in order to come to a quicker resolution. 

For the scenarios the DRIs were unable to solve, we see that as an opportunity to improve the available tools. This is specifically prominent in searching by a customer's Resource URI - which we plan releasing a new feature in [FCM Change Explorer](https://aka.ms/FCM) where users will have the ability to search by resource URI and subscription ID. 

Additional findings showed that some of the dashboards used by DRIs to quickly look up customers were limited to only Walmart - [OneDeploy Walmart Dashboard](https://dataexplorer.azure.com/dashboards/95963854-b111-4680-a16f-9f3383d49f9b?p-_startTime=2days&p-_endTime=now&p-_measure=all&p-_payload=all&p-_tag=all&p-_impact=v-All&p-_region=all&p-_ve=all&p-_noflyzone=all&p-_RoleInstanceName=all&p-_nodeid=all#c676ca09-727b-4124-ab01-8e3782e191f9). We took action on this and we developed a new dashboard that contains S500 customers which is now available here - [OneDeploy Dashboard](https://aka.ms/AzChangeManagement)

## Scenarios

[Finding Node Level Changes](https://eng.ms/docs/products/fcm-engineering-hub/ace_dri/findnodelevelchanges)

[Finding Changes within a specific Region, Customer and Time Range](https://eng.ms/docs/products/fcm-engineering-hub/ace_dri/regioncustomertimechanges)

[Finding Changes with a Specific Resource URI and Time Range](https://eng.ms/docs/products/fcm-engineering-hub/ace_dri/resourceuritimechanges)



See anything we missed? We would love to hear your feedback or additional scenarios to add to this site. To do so, please contact our PM [Alyssa Kay](mailto:alyssa.kay@microsoft.com?subject=Wiki%20Request:%20[Team%20Name])

### Points of Contact

- Mark Citron, SDM: mark.citron@microsoft.com
- Alyssa Kay, PM: alyssa.kay@microsoft.com

<!--Here you will find information on how to accurately navigate an incident in order to assign it to the correct team

List of tools ACE DRIs currently use, pain points we have observed, how we can address those pain points -->