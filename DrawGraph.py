import networkx as nx
import time


def generateGraph(data, roundLimit):
    start = time.time()
    print("Start generating graph...")
    G = nx.Graph()
    G.add_weighted_edges_from(data[1])
    print("Graph generated in: " + str(round(time.time() - start, roundLimit)) + "\n")
    return G
