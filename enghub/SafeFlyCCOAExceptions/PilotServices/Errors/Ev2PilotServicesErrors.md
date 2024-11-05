# If an Error Occurs: Fallback Plan for QCS Ev2 Services

If you are a service that is QC, uses Ev2 as a deployment system and is onboarded to R2D, this page will provide the information to help navigate any issues. Below is an image of the decision path for this user experience.

![alt text](media/E2E_Ev2.png)

If an error occurs and the service is unable to submit a CCOA exception request, SafeFly will manually bypass the CCOA deployment block. Upon receiving and error or faced with the inability to submit an exception request in SafeFly, the person submitting the request should create an ICM, assign it to the SafeFly team and provide the SafeFly ID in the ICM. An ICM template is available [here](https://portal.microsofticm.com/imp/v3/incidents/create?tmpl=Q3x1H3).

Our on call engineers will conduct an investigation and will add your service to the approved services list. The deployment will then be unblocked and ready to roll out.

QCS Ev2 services will not be able to submit an exception request in Change Guard without intervention from the Change Guard team. If they attempt to submit a CCOA request in the Change Guard portal instead of SafeFly, they will receive the following error that contains a link to the R2D form.

![alt text](media/SF_5.png)