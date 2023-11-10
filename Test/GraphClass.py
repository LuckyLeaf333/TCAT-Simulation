import matplotlib.pyplot as plt
import networkx as nx
import math

class Bus:
    
    def __init__(self, number, route, capacity, pos, labels):
        #Route number (for example route 30 etc)
        self.number = number

        #Edges to represent the path the route takes
        self.route = route

        #Capacity of the bus
        self.capacity = capacity

        #position of the nodes
        self.pos = pos
        
        #Potenital attributes
        self.labels = labels


    def initialize(self):
        for i, j in self.route.edges:
            #basically assign the edge the bus number that will travel on it
            self.route.edges[i, j]['number'] = self.number
        self.labels = {}

        for i, j in self.route.edges:
            self.labels[(i,j)] = str(self.number)
        
    def show(self):
        nx.draw_networkx(self.route,self.pos,node_size=500,node_color='darkorange') # draw graph
        nx.draw_networkx_edge_labels(self.route,self.pos,edge_labels=self.labels)
        
route = nx.Graph()
edgeList = [(1, 2), (2, 3), (3, 5), (5, 6), (6, 1)]
route.add_edges_from(edgeList)
pos = ((0,0),(0,10),(10,20),(10,0),(30,20),(30,0),(40,10))
newBus = Bus(30, route, 3, pos, 0)

newBus.initialize()
newBus.show()
plt.show()
