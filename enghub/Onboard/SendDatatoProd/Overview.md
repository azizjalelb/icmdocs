# How to send data to FCM Production

If you have validated the flow in PPE completely then the next step would be to move to production for this. Recommendation is to run it in PPE for a week and try different values and scenarios for Change Events.  

Here are the steps to start sending the changes to FCM Production: 

[Step 1](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#Register-an-external-source-with-FCM ) Register an external source with FCM  

[Step 2](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#adding-your-application-to-azure-active-directory) Adding your application to Azure Active Directory 

[Step 3](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#daily-change-volume-to-fcm-estimate) Daily change volume to FCM estimate 

[Step 4](https://eng.ms/docs/products/fcm-engineering-hub/onboard/SendDatatoProd/sendingdata#fcm-prod-account-information) FCM Prod account information 

We have a sample solution available [here](https://microsoft.sharepoint.com/:u:/r/teams/WAG/EngSys/ServiceMgmt/ChangeMgmt/Shared%20Documents/Send%20ChangeEvent%20Using%20IFX%20Agentless/ChangeEventSender-NetStd.zip?csf=1&web=1&e=M9e3Um) to provide an additional example for sending change event data to FCM