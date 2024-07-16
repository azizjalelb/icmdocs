# ICM Event Processor (IEP)

## Overview
IEP is an eventhub triggered Azure Function. It reads the incident events from ICM Event hub as they got ingested to the event hub. IEP is responsible from: 
1) Reading incident event data from ICM event hub
2) Getting the changes that could have caused that incident from GetIncidentChanges API
3) Updating the discussion of an incident with those changes or with "No changes found" if FCM didn't find any changes for the search criteria of that incident.

## Criteria for Processing Incidents
IEP doesn't try to get changes for all the incidents that is created in ICM. Currently, IEP processes an ICM event if:

1) incident is active and
2) incident has severity <=2 and
3) incident owning service tree id is not excluded (currently only excluded ServiceTreeId is `53ed86d2-2404-43b0-b7be-903b45386319`) and 
4) incident is an Azure incident

## Criteria for Updating Incidents
IEP updates the discussion of the incidents either with 
1) set of changes that we found for the search criteria of the incident or 
2) with 'No changes found.' for the search criteria of the incident. 

### Updating Incidents With Changes
By design, multiple events per incident will be ingested into ICM Eventhub and IEP will read all of them and process it if the event satisfies our criteria to process incidents. 

However, IEP updates an incident with changes only if the incident hasn't been already updated with same set of changes. We guarantee this condition by 
1) ordering the changes based on their rank (which is determined by the proximity of the change to the incident start time. Change that happened closer to the incident start time is ranked higher) and 

2) picking up a maximum number of changes to show, which is currently set to be 10 and storing these changes for that incident in a Redis cache.

3) Before we update an incident with set of change, we check the cache to see if the incidet has already been updated with the same set of changes.


### Updating Incidents With "No changes found."
IEP will update an incident with "No changes found." only if there has been more 60 minutes since the incident has started. This because we have a latency when ingesting change events into FCM. If we update the incidents with "No changes found." without considering this ingestion latency, we will end up in a scenario which we will update an incident with "No changes found." and then, we will update the same incident with a set of changes which came delayed due to ingestion latency and this will confuse the DRIs who are trying to mitigate the incident.



## Preventing Multiple Updates to Same Incident
As IEP reads events from ICM Eventhub as they get ingested to the event hub, due to the race conditions, IEP would process multiple events for the same incident, call GetIncidentChangesAPI to get relevant changes and then, try to update the incident discussion with same set of changes multiple times. However, this will create a noise in the incident discussion and can cause the DRI to miss the relevant information when working on mitigating an incident.

In order to prevent this, IEP uses [leasing with Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-lease). In Azure Blob storage, currently we have 256 containers to be used for leasing. When a thread starts processing an incident event, we determine which container it should lease by computing `IncidentId % 256`. 

#### **Scanario 1: Container is available for a thread to acquire it for leasing.**
The processing thread acquires the lease for that container if the container is not already leased and holds for a maximum of 59 seconds. Once it processes the incident, it releases the lease so that other threads can pick it up. 

#### **Scenario 2: Container is already leased, the thread has to wait.**
If the processing thread has to wait for a container to acquire a lease, it will keep checking whether the container becomes available in loop. If the same lease is present in the container for more than *TimeToBreakLeaseInSeconds* (currently set to be 60 seconds), it will break the lease for that container and make the container available to be leased by another thread. However, this doesn't guarantee that the thread that broke the lease of a container will lease the container as another thread which is waiting for the same container can come and lease that container before the first thread does. In that case, the first thread will keep waiting in the loop again for the container to become available again to be leased. However, this might cause the thread to wait in the loop until the Function App timeouts which is 30 minutes. Since the thread can get stuck in the same loop until the function timeout of 30 minutes, it will not be able to pick up new events from event hub to process and that it will increase our latency to process inciden events. Thus, we added a logic which makes sure that if a thread is waiting to acquire for a lease for more than 2 minutes, we will issue a dummy lease and let the thread go and process the incident event. This might cause an incident to be updated more than once but since this is an edge case, it won't happen often.