# Sending Change Events to FCM Overview

Microsoft teams have custom tools to orchestrate their releases, code and data deployments and configuration changes. These tools can send change data to FCM to enable teams to gain insights into changes to their service and environment. FCM provides ChangeEvent schema, Azure Queue and API endpoints to send these events. 

To learn more on how to send Change Events to FCM and to understand the architecture behind it, please check out our quick links below 

## Sending Changes to FCM PPE:

[Get IFX Agentless (Eventrouter) bits](https://eng.ms/docs/products/fcm-engineering-hub/onboard/sendingchangestoppe/ifxagentless)

[Create appid and associate certificate](https://eng.ms/docs/products/fcm-engineering-hub/onboard/sendingchangestoppe/createappid)

[Write the code to send Change Event](https://eng.ms/docs/products/fcm-engineering-hub/onboard/sendingchangestoppe/writecode)

[Validate changes are Sent](https://eng.ms/docs/products/fcm-engineering-hub/onboard/sendingchangestoppe/validatechanges)

## Sending Data to FCM Production
[Register an external source with FCM](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#Register-an-external-source-with-FCM)

[Adding your application to Azure Active Directory](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#adding-your-application-to-azure-active-directory)

[Daily change volume to FCM estimate](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#daily-change-volume-to-fcm-estimate)

[FCM Prod account information](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#fcm-prod-account-information)

## Data Field Descriptions
[Change Event Field Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/changeeventdesc)

[ChangeType (ActionName) Field Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/changetype)

[Status Name Field Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/statusnamedesc)

[Environment Field Descriptions](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/environmentdesc)

[Location Types](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/locationdesc)

[DateTime Formatting](https://eng.ms/docs/products/fcm-engineering-hub/onboard/datafielddesc/datetimeformatting)

## Further Guidance 
To save this information, you can also refer to our documentation [Sending Change Events using IFX Agentless](https://microsoft.sharepoint.com/:w:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/_layouts/15/Doc.aspx?sourcedoc=%7B703F0892-7E8A-417D-97B9-DC1B1308F6F8%7D&file=Sending%20ChangeEvent%20using%20IFX%2009_30_16.docx&action=default&mobileredirect=true&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2Calkay%40microsoft.com&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzAxMTUwMDkwNyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&cid=f09de021-bdfe-4870-aa62-7868429d1d9b)

*Note: this documentation has been formatted and is available on this wiki site*

If you need assistance with the sending out change events in FCM, please refer to our [FAQs](https://eng.ms/docs/products/fcm-engineering-hub/faq/sendingdataFAQ) or email [FCM Support](mailto:fcmsupport@microsoft.com?subject=Onboarding%20Request:%20[Team%20Name])