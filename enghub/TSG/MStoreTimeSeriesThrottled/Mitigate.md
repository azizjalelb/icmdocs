# Mitigation steps for MStoreTimeSeriesThrottled Failure

1) Visit MdmQos dashboard https://jarvis-west.dc.ad.msft.net/dashboard/changemds/GenevaQos/%25E2%2586%2590%2520MdmQos 
2) check current number of time series, limits and number of dropped samples
    * If the increase in number of active time series is expected, request an increase to your current limit by visiting: https://jarvis.dc.ad.msft.net/?page=settings&mode=mdm&tab=account&section=accountLimitRequest&account=changemds.

 > [!Note] 
 The number of active time series in account changemds is 95% of the limit. Current: 482138 Limit: 500000. Exceeding the limit may result in new time series being throttled and data for them dropped, which can cause a loss of monitoring capabilities. No data loss is occurring at this time. 