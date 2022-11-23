import networkx as nx
from pyvis.network import Network

def build_graph(collace_edge):

    #print(collace_edge)
    G=nx.DiGraph()
    G.add_edges_from(collace_edge)

    net = Network()
    net.from_nx(G)

    net.show_buttons()
    net.show("checkcallingmy.html")
