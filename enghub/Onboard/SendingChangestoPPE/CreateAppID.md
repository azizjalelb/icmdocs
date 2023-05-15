# Step 2: Create appid and associate certificate 

Create app in AAD and associate a cert with the app for authentication. Pass on the appid to FCMSupport for onboarding. 

*Note: Make sure the cert is from a valid issuer, and associate your app with the subjectname of the  cert, this enables auto rotation of your cert.*  

You can use DSO tool Workspace Applications | Geneva Analytics User Documentation (msftcloudes.com) and follow step 1 to associate cert with app. (only step1 is required, other steps are not required). 