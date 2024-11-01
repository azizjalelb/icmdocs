from diagrams import Cluster, Diagram, Edge

from diagrams.azure.network import VirtualNetworks
from diagrams.azure.compute import FunctionApps
from diagrams.azure.network import FrontDoors
from diagrams.azure.web import AppServiceEnvironments
from diagrams.azure.web import AppServicePlans
from diagrams.azure.integration import APIManagement
from diagrams.azure.network import ApplicationGateway
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.network import PrivateEndpoint
from diagrams.azure.identity import ManagedIdentities
from diagrams.azure.compute import ContainerInstances
from diagrams.azure.network import Subnets
from diagrams.azure.network import PublicIpAddresses
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.network import Firewall
from diagrams.azure.devops import Repos, Pipelines
from diagrams.azure.security import KeyVaults
from diagrams.azure.database import DataExplorerClusters

graph_attr = {
    "layout":"dot"
}

with Diagram("Network Isolation", graph_attr=graph_attr, show=False):

    # resources outside of the vnet
    st = StorageAccounts("st")
    appi = ApplicationInsights("appi")
    appiafd = ApplicationInsights("appi-afd")
    law = LogAnalyticsWorkspaces("law")
    afd = FrontDoors("afd")
    fw = Firewall("fw")
    aci = ContainerInstances("aci")
    id = ManagedIdentities("id")
    kv = KeyVaults("kv")
    db = DataExplorerClusters("db")

    # resources within the vnet
    with Cluster("vnet", direction="LR"):
        agw = ApplicationGateway("agw")
        # resources within the ase
        with Cluster("ase"):
            # resources for the func
            asp = AppServicePlans("asp")
            func = FunctionApps("func")
        # subnets for the vnet
        with Cluster("subnets", direction="LR"):
            subaci = Subnets("sub-aci")
            subfunc = Subnets("sub-func")
            subapim = Subnets("sub-apim")
            subagw = Subnets("sub-agw")
            subst = Subnets("sub-st")
        # resources for the apim
        with Cluster("apim"):
            apim = APIManagement("apim")
            pip = PublicIpAddresses("pip")
        # private endpoints
        pepagw = PrivateEndpoint("pep-agw")
        pepst = PrivateEndpoint("pep-st")

    # ado
    aci - Edge() - id
    aci >> Edge(color="green", style="bold") >> subaci

    # afd
    afd - Edge() - fw
    afd >> Edge(color="green", style="bold") >> appiafd
    afd >> Edge(color="green", style="bold") >> pepagw
    pepagw >> Edge(color="blue", style="bold") >> subagw
    appiafd >> Edge(color="green", style="bold") >> law

    # agw
    agw >> Edge(color="yellow", style="bold") >> subapim

    # apim
    pip - Edge() - apim
    apim >> Edge(color="green", style="bold") >> appi
    apim >> Edge(color="blue", style="bold") >> subfunc

    # func 
    func - Edge() - asp
    func >> Edge(color="green", style="bold") >> appi
    func >> Edge(color="green", style="bold") >> db
    func >> Edge(color="green", style="bold") >> kv

    # storage account
    appi >> Edge(color="green", style="bold") >> law
    st >> Edge(color="green", style="bold") >> pepst
    pepst >> Edge(color="blue", style="bold") >> subst