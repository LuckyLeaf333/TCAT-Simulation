# imports
import networkx as nx
import matplotlib.pyplot as plt

# G is an undirected graph
G = nx.Graph()

# Edge (1,2) is a road from stop 1 to stop 2
edgeList = [(1, 2), (2, 3), (1, 3)]

# Create the graph based on this list.
G.add_edges_from(edgeList)

nx.draw(G) # draw graph
plt.show()