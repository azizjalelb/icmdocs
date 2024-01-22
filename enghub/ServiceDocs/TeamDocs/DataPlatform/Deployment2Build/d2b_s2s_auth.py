from adal import AuthenticationContext
import requests

authority = 'https://login.microsoftonline.com/'
tenant = '72f988bf-86f1-41af-91ab-2d7cd011db47' # msft tenant
client_id = '' # app id of your service
client_secret = '' # secret; can use other auth methods (like cert) as  well
resource = 'api://b565c703-fa73-48d1-92cf-a002721abe2e' # scope 

d2b_api_endpoint = 'http://afd-dataplatform-int-apegeggveef0apbq.z01.azurefd.net/d2b/builds'
deploymentId = 'ContainerService/b03fe328-9f11-42c4-8eed-73a0f0d1c944'
deploymentSource = 'expressv2'

auth_context = AuthenticationContext(authority + tenant)

token = auth_context.acquire_token_with_client_credentials(resource=resource, client_id=client_id, client_secret=client_secret)

params = {
    'deploymentId': deploymentId,
    'deploymentSource': deploymentSource,
}

headers = {
    'Authorization': 'Bearer ' + token['accessToken']
}

request = requests.get(d2b_api_endpoint, params=params, headers=headers)

print(request.text)