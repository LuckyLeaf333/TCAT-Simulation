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

        # self.currentpass = []
        #     for i in range(cap):
        #         self.currentpass.append(0)
        #     print(self.currentpass)
        
        # self.currentpass = np.empty(cap, dtype = Passenger)
            # change array to maybe an array of Passenger objects?


# a = Bus(1234,81,10,1,2)
    
#      def bus_full (busNum):
#          if (self.numPass == self.cap)
#              return true
#          else return (self.cap-self.numPass)

