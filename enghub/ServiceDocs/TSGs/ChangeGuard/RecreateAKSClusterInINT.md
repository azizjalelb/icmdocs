# The scenario will present the steps of recreating the AKS cluster on INT environment after an accidental deletion

### Notes:
- In this scenario we assume that all other objects are already in place and configured (Key Vault, secrets, certificates, Public IP, etc) and we are only focusing on the AKS cluster.
- Prepare your environment by installing:
  - [Powershell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)
  - [Az CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)
  - [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/) 
  - [Helm](https://helm.sh/docs/intro/install/)
- All commands are to be run in a terminal (Windows Terminal)

### Step 1: Set up the environments variables and log into Azure
Go to `FCM-ChangeManager\src\Infrastructure - INT` and run the powershell script `step-00-global.ps1`

### Step 2: Create AKS Cluster
```
az aks create --resource-group $RG_Name --name $AKS_Name --node-count 3 --generate-ssh-keys --attach-acr $ACR_Name --dns-name-prefix $global:AKS_Dns_Name_prefix --load-balancer-sku standard --enable-managed-identity
```

### Step 3: Get the Service Principal ID for AKS Cluster
```
$AKS_ServicePrincipal = az aks show -g $RG_Name -n $AKS_Name --query "identity.principalId" -o tsv
```

### Step 4: Ensure the service principal used by the AKS cluster has delegated permissions to the resource group
```
az role assignment create --assignee $AKS_ServicePrincipal --role "Network Contributor" --scope
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RG_Name
```

### Step 5: Login to cluster to generate context
```
az aks get-credentials --name $AKS_Name --resource-group $RG_Name --overwrite-existing
```

### Step 6: Create K8s namespace
Go to `FCM-ChangeManager\src\Infrastructure - INT` and run
```
kubectl apply -f .\changemanager-ns.yaml
```

### Step 7: Install the secret provider driver for AKS, using helm
```
helm repo add csi-secrets-store-provider-azure https://azure.github.io/secrets-store-csi-driver-provider-azure/charts
helm repo update
helm install azurekeyvault-csi-secret-provider csi-secrets-store-provider-azure/csi-secrets-store-provider-azure -n changemanager-ns 
```

### Step 8: Get Service principal Id and Password from Key Vault
```
$AKS_SP_APPId = az keyvault secret show --vault-name $global:KeyVault_Name --name "aks-sp-appid" --query "value" -o tsv
$AKS_SP_Pwd = az keyvault secret show --vault-name $global:KeyVault_Name --name "aks-sp-pwd" --query "value" -o tsv
```

### Step 9: Create Kubernetes secret to enable access to Keyvault
```
kubectl create secret generic secrets-store-creds --from-literal clientid=$AKS_SP_APPId --from-literal clientsecret=$AKS_SP_Pwd -n changemanager-ns
```

### Step 10: Deploy certificate maps and cluster services to the AKS cluster
Go to `FCM-ChangeManager\src\Infrastructure - INT` and run
```
    kubectl apply -f .\changemanager-secrets-map.yaml --namespace changemanager-ns
    kubectl apply -f .\changemanager-ingress-certs-map.yaml --namespace changemanager-ns
    kubectl apply -f .\changemanager-workflow-urls-map.yaml --namespace changemanager-ns
    kubectl apply -f .\changemanager-cxpretrieval-certs-map.yaml --namespace changemanager-ns
    kubectl apply -f .\changemanager-ingress-whitelistedclients-map.yaml --namespace changemanager-ns
    kubectl apply -f .\changemanager-services.yaml --namespace changemanager-ns
```    

### Step 11: Deploy application code to the AKS cluster 
Go to `FCM-ChangeManager\src\ServiceGroupRoot\AzureKubernetesService\Deployment` and run
```
kubectl apply -f .\changemanager-deployment-INT.yaml --namespace changemanager-ns
```

### Step 12: Add the admin kubeconfig for the cluster to Key Vault:
Follow the instructions from [Make sure you generate an admin kubeconfig for the cluster and add it to KV:](EnvironmentSetupTSGs.md).

### Step 13: Test that all of the pods are in a healthy state
```
kubectl get pods -n changemananger-ns
```
The documentation on how to test each part of the system can be found in
the [README.md](https://msazure.visualstudio.com/One/_git/FCM-ChangeManager?path=/src/README.md) file inside the repo.

> [!NOTE]
> For any issues check the [TSG for Environment Setup](EnvironmentSetupTSGs.md).