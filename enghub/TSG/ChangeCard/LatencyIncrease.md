# P90 Latency increase in changecard

### Overview

Latency Increase in Change Card is usually caused when there is Kusto performance degaradation. If there is a Kusto performance degradation with no increase in the query count, we have to raise ICM with Kusto Team using [Gaia Bot](https://bot-gaiaprod-website.azurewebsites.net/resources/site/gaia.html).

[Sample Incident](https://portal.microsofticm.com/imp/v3/incidents/details/379040414/home) Raised with Kusto Team.

First Step is to check the Kusto Performance. Please follow the link to check [PROD Kusto Health](https://jarvis-west.dc.ad.msft.net/dashboard/share/DB99F283?overrides=[%7B%22query%22:%22//*[id=%27Account%27]%22,%22key%22:%22regex%22,%22replacement%22:%22*%22%7D,%7B%22query%22:%22//*[id=%27Cluster%27]%22,%22key%22:%22value%22,%22replacement%22:%22FCMDATA%22%7D,%7B%22query%22:%22//dataSources%22,%22key%22:%22account%22,%22replacement%22:%22KustoCentralUS%22%7D,%7B%22query%22:%22//*[id=%27Account%27]%22,%22key%22:%22value%22,%22replacement%22:%22%22%7D]%20) 


- Check for CPU Usage
- Check for Concurrent Queries
- Check for Query Duration
- Check for Query Count

If there is an increase in the number of queries executed over the past two days and if the current active nodes are not able to handle the load, try increasing the number of active nodes from the Azure Portal on SAW machine.


### Kusto Queries to analyze further on what is being executed in PROD.
#### Memory Usage 
'.show commands-and-queries
| where StartedOn >ago(5d)
| summarize sum(MemoryPeak) by User, bin(StartedOn, 10m)
| render timechart'

#### Query Count by User
'.show commands-and-queries
| where  StartedOn>ago(5d)
| summarize count() by bin(StartedOn, 1h), User
| render timechart'

#### CPU Usage
'.show commands-and-queries   | where StartedOn > ago(5d)
| summarize sum(TotalCpu) by User ,bin(StartedOn, 1h)
| render timechart'
