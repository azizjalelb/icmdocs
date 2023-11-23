## Summary
[FCM ChangeMetrics dashboard](https://aka.ms/fcmchangemetrics) is used to track and improve the quality of the change data ingested into FCM Kusto.

Key quality attributes we measure are latency, data quality for Payload, Entity, Region, StartTime, EndTime. A Maturity Score is assigned at the dataquality attribute level in the weekly and monthly email reports, but the Maturity level is defined at Service level in the dashboard for better readibility.

### Maturity Level

Maturity Level in the Email Reports:
- Maturity Level is defined at the data quality attribute in the email reports.
- There are three different levels of Maturity
    - Maturity Level 3 - This is when we have ~100% good quality data for the given data quality attribute.
    - Maturity Level 2 - This is when we have ~50-99% good quality data for the given data quality attribute.
    - Maturity Level 1 - This is when we have ~0-50% good quality data for the given data quality attribute.

- Maturity Level is defined at the Service Level in the [FCM ChangeMetrics dashboard](https://aka.ms/fcmchangemetrics)
- There are three different levels of Maturity at Service Level as well
    - Maturity Level 3 - This is when we have ~0-1% of Invalid data for the Payload, Entity, StartTime and EndTime.
    - Maturity Level 2 - This is when we have ~1-50% of Invalid data for the Payload, Entity, StartTime and EndTime.
    - Maturity Level 1 - This is when we have ~50-100% Invalid data for the Payload, Entity, StartTime and EndTime.


### Change Metrics Email Reports
We generate Weekly and Montly FCM ChangeMetrics Reports at the Service Level. There are basically three tables of data we provide in that

Table 1: Service Level Data. This Table consists of Service Name, TotalRowCount, IngestionLatency95(in minutes).

Table 2: Weekly/Monthly Maturity Score by the Service, Source, DataQuality Attribute.

Table 3: Missing Change Attributes. This table consists of ServiceName, Source, TotalRowCount, DataQualityAttribute, InvalidDataCount, MaturityScore, SampleInvalidData and DeepLinkForSampleInvalid Data.


Please note that the DeepLinks are not generated for the Empty InvalidData. For Example, if we are receiving empty payloads or entities, then the deeplink will not be generated. In that scenario, below queries can be used to view the data in the fcm kusto. 
1. For Source Systems: expressv2, adorelease, xstore-wadi, xstore-xds and for Services: MDM and Corewan


2. For any other Source System data;

