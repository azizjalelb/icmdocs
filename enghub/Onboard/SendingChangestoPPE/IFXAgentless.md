# Step 1: Get IFX Agentless (Eventrouter) bits 

## For public cloud 

Get the latest IFX Agentless (Eventrouter) bits as nuget. You can get the bits from nuget repository. 


<span style="font-family:Courier New; color:orange;">For .Net Framework - Microsoft.Cloud.InstrumentationFramework.EventRouter.amd64 package is available @feed https://msazure.pkgs.visualstudio.com/_packaging/Official/nuget/v3/index.json</span>
 

<span style="font-family:Courier New; color:orange;">For .Net standard  - Microsoft.Cloud.InstrumentationFramework.EventRouter.NetStd package is available @feed https://msazure.pkgs.visualstudio.com/_packaging/FCM/nuget/v3/index.json </span>

*Note : Currently .Net std supports only Microsoft tenant*

**Get the latest IFX Agentless (Eventrouter) bits as nuget. You can get the bits from nuget repository listed above.** 

<span style="font-family:Courier New; color:orange;">Install-Package Microsoft.Cloud.InstrumentationFramework.EventRouter.amd64 </span>

<span style="font-family:Courier New; color:orange;">Install-Package Microsoft.Cloud.InstrumentationFramework.VC14 </span>

And your solution folder should look like this with all the required dll: 

![alt text](media/ifx_01.png)