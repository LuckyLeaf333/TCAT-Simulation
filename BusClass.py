import matplotlib.pyplot as plt
import networkx as nx
import math

class Bus:
    
    def __init__(self, route, cap, numPass, node):

        #Route number (ex. Route 30)
        self.route = route

        #Capacity of the bus
        self.cap = cap

        #number of passengers currently on the bus
        self.numPass = numPass

        #The current node the bus is at
        self.node = node
    
    # def bus_full (busNum):
    #     if (self.numPass = self.cap)
    #         return true
    #     else return (self.cap-self.numPass)

    # def 