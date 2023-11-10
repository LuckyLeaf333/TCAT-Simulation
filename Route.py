import matplotlib.pyplot as plt
import networkx as nx
import math


class Route:

    def __init__(self, nodes, edges, number, positions, times):
        # A list of nodes, representing bus stops, included in the route
        self.nodes = nodes

        # A list of edges in the route
        self.edges = edges

        # A unique number identifying the route
        self.number = number

        # A list of (x,y) coordinates for drawing the nodes
        self.positions = positions

        # A networkx graph representing the route
        self.graph = nx.Graph()
        self.graph.add_edges_from(self.edges)

        i = 0
        for (u, v) in self.graph.edges():
            self.graph[u][v]['times'] = times[i]
            i += 1

    def numStops(self):
        return len(self.nodes)

    def show(self):
        nx.draw_networkx(self.graph, self.positions, node_size=500, node_color='darkorange')  # draw graph
        nx.draw_networkx_edge_labels(self.graph, self.positions,
                                     edge_labels=nx.get_edge_attributes(self.graph, 'times'))
        plt.show()


# nodes = (1, 2, 3, 4, 5, 6)
# edgeList = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# positions = ((0, 0), (0, 10), (0, 20), (30, 20), (30, 40), (40, 50), (50, 60))
# times = [5, 10, 7, 9, 8]
#
# testRoute = Route(nodes, edgeList, 30, positions, times)
# testRoute.show()
# print(testRoute.numStops())
