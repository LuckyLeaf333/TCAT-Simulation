import matplotlib.pyplot as plt
import networkx as nx
import math

class Bus:
    
    def __init__(self, route, cap, node):

        #Route number (ex. Route 30)
        self.route = route

        #Capacity of the bus
        self.cap = cap

        #number of passengers currently on the bus
        self.numPass = 0

        #The current node the bus is at
        self.node = node

        self.time_ = 0

        

    
    def update_time(self):
        self.time_ += 1
    
    def reset_time(self):
        self.time =0

    def time(self):
        return self.time_
    
    def return_route(self):
        return self.route
    
    def return_node(self):
        return self.node

    def update_node(self, number):
        self.node = number
    
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

