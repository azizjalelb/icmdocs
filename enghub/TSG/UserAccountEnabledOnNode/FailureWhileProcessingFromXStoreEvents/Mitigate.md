

# Mitigation steps for failures while processing from XStore Events
1)  Login to Azure Portal with your AME Credentials.

2) Go to Function App, find "xstoreeventprocessoreast", click on it, and go to Application Insights for this function app from the panel on the left. The Application Insights is called "mdseventprocessorlogs".

3) Look for exceptions for Xstore by running the query below in the "Logs" tab:

    ```
    exceptions 
    | where problemId contains("xstore") 
    | order by timestamp desc
    ```

![xstoreFailureMitigation](../Images/xstoreFailureMitigation.png)

4) Take necessary action as per the error messages. 






