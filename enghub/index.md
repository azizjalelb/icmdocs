# Federated Change Management

## What is Federated Change Management (FCM)?

Federated Change Insights aggregates standardized change data streams from change orchestrators and enables On-call Engineers and service owners to diagnose and mitigate service impacting issues, by providing observability to all changes ongoing in Azure which is essential for any cloud platform to succeed. Core capabilities:-

#### Change Standardization

- **Aggregates standardized change events** with a standardized [Entity Model](https://microsoft.sharepoint.com/:w:/t/SilverstoneProject/Eeqg50_nDm1ItTXBogvLcq8BybpPWO41X2Yq7FG-UTHlAA?e=5VSivg) across Microsoft with SLA bound quality and latency.
- **Automated ingestion and onboarding** for standard deployment platforms such as AzDeployer, Pilotfish, EV2, OaaS, GenevaActions etc. Services with Custom change providers onboard using standard [EM SDK](https://eng.ms/docs/products/fcm-engineering-hub/servicedocs/teamdocs/onboarding/entitymodelchangeeventssdk) (Datacenter maintenance, Network device updates etc).

#### Change Visibility (#FogOfWar)

- **Layered actionable visibility** with [drill down views](https://dataexplorer.azure.com/dashboards/d0357802-00ae-48c7-85a2-5cf02d98de77?p-_startTime=1hours&p-_endTime=now&p-_nodeid=all&p-_entityTypeNode=all&p-_changeType=all#08c31477-dfa3-43d3-9427-a6a57b228c43) for Compute/Networking/Storage topology for physical and logical capacity of the Azure fleet and the changes being orchestrated, along with Payload SDP progression and SDP bypasses.
- **Contextual ICM** **Integration** to show changes in incident discussions, Obi and Troubleshooting Studio. Utilizes AI to summarize changes happening in the platform.
- **Proactive deployment stops** providing ability for Incident Managers to Pause/Abort a deployment in the event of an outage.

### Points of Contact

- Naveen, SDM: naveend@microsoft.com
- Usha, PM: ushapinreddy@microsoft.com
- FCM Support: fcmsupport@microsoft.com

## Quick Links

### Getting Started

[Onboarding to FCM](https://eng.ms/docs/products/fcm-engineering-hub/onboard/description)

[FCM Architecture](https://eng.ms/docs/products/fcm-engineering-hub/onboard/fcmarchitecture/fcmarchitecture)

[Sending Change Events to FCM](https://eng.ms/docs/products/fcm-engineering-hub/onboard/fcmarchitecture/fcmarchitecture)

[Change Explorer Overview](https://eng.ms/docs/products/fcm-engineering-hub/changeexplorer/changeexploreroverview)

[Change Guard Overview](https://eng.ms/docs/products/fcm-engineering-hub/changeguard/changeguardoverview)

### How to

[Kusto Access](https://eng.ms/docs/products/fcm-engineering-hub/onboard/fcmarchitecture/kusto/kusto)

[Lens Access](https://eng.ms/docs/products/fcm-engineering-hub/onboard/fcmarchitecture/lensexplorer)

[Submit an Exception Request in Change Guard](https://eng.ms/docs/products/fcm-engineering-hub/changeguard/gettingstarted)

<!--UPDATE-->

### Troubleshooting

[FCM Onboarding FAQs](https://eng.ms/docs/products/fcm-engineering-hub/faq/faq)

<!--[Change Guard Exception Requests FAQs]()-->

### Links and Resources

| Resource | Link |
| --- | --- |
| FCM Change Explorer | https://aka.ms/fcm |
| Change Guard | https://aka.ms/changeguard |
| Kusto Explorer | https://fcmdataro.kusto.windows.net:443 |