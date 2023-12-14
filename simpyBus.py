import simpy
import matplotlib.pyplot as plt
import networkx as nx
import csv


class Passenger:

    """
    id: Unique id number of the passenger
    start: The bus stop the passenger begins at
    target: The bus stop the passenger wants to go to
    """
    def __init__(self, id, start, target):
        self.id = id
        self.start = start
        self.target = target
        
    def return_node(self):
        return self.start


class Bus(object):

    """
    env: SimPy environment simulation runs in
    id: unique id number of the bus
    capacity: Maximum number of passengers the bus can have
    stopList: A list of the stops along the bus' route. Assumes the route is a cycle
    graph: A graph of the stops in the bus system. The stopList must contain a valid cycle in this graph.
    """
    def __init__(self, env, id, capacity, stopList, graph):
        self.env = env
        self.id = id
        self.capacity = capacity
        self.numPassengers = 0
        self.stopList = stopList
        self.graph = graph
        self.stopIndex = 0
        self.stopName = self.stopList[self.stopIndex]
        self.passengerList = []

        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    """
    Get the index of the next stop in stopList. Loops back to the beginning of the stopList when the end is reached.
    Assumes the route is a loop.
    """
    def nextStopIndex(self):
        if self.stopIndex == len(self.stopList) - 1:
            return 0
        return self.stopIndex + 1

    """
    Make the bus travel along its route. Pick up and drop off passengers if appropriate.
    Report when the bus leaves a certain stop.
    """
    def run(self):
        while True:
            # Travel to next stop
            nextStopName = self.stopList[self.nextStopIndex()]
            yield self.env.process(self.goToNextStop(graph[self.stopName][nextStopName]['time']))

            # Board passengers if bus not full
            if self.numPassengers < self.capacity:
                yield self.env.process(self.pickUpPassengers(5))

            # if there are passengers to drop off, drop off the passengers
            yield self.env.process(self.dropOffPassengers(5))
            print("Bus %d is leaving stop %s at time %d" % (self.id, self.stopName, self.env.now))

    """
    Move the bus to its next stop. Report when the bus arrives at its next stop.
    duration: The amount of time it takes to travel to the next stop.
    """
    def goToNextStop(self, duration):
        yield self.env.timeout(duration)
        self.stopIndex = self.nextStopIndex()
        self.stopName = self.stopList[self.stopIndex]
        print("Bus %d has arrived at stop %s at time %d" % (self.id, self.stopName, self.env.now))

    """
    Pick up passengers at the current stop if there are passengers to pick up. 
    Reports which passengers are picked up, if any.
    duration: The amount of time it takes to board passengers 
    """
    def pickUpPassengers(self, duration):

        stopPassengerList = self.graph.nodes[self.stopName]['passengers']

        # Make a list of passengers waiting at current stop which want to go to a location
        # which this bus goes to
        passengersToBoard = []
        for passenger in stopPassengerList:
            if passenger.target in self.stopList:
                passengersToBoard.append(passenger)

        # Leave immediately if no passengers at the stop want to get
        if len(passengersToBoard) == 0:
            return

        outputString = ""
        while self.numPassengers < self.capacity and len(passengersToBoard) > 0:
            # Remove a passenger from the boarding list
            passenger = passengersToBoard.pop()

            # Remove the passenger from the waiting set at the bus stop
            stopPassengerList.remove(passenger)

            # add passenger to the bus
            self.passengerList.append(passenger)
            self.numPassengers = self.numPassengers + 1
            outputString += str(passenger.id) + ", "

        # Boarding takes a certain amount of time
        yield self.env.timeout(duration)
        print("Bus %d has boarded passengers %sat time %d" % (self.id, outputString, self.env.now))

    """
    Drop off passengers, if the current stop is the passengers' destination.
    Report which passengers were dropped off, if any.
    duration: The amount of time it takes to drop off passengers.
    """
    def dropOffPassengers(self, duration):
        dropOff = False  # True if any passengers should be dropped off
        dropOffList = []  # List of passengers to drop off

        for passenger in self.passengerList:
            # Determine if any passengers should be dropped off
            if passenger.target == self.stopName:
                dropOff = True
                dropOffList.append(passenger)

        if dropOff:
            # Drop off passengers in dropOffList
            yield self.env.timeout(duration)
            outputString = ""
            for passenger in dropOffList:
                self.passengerList.remove(passenger)
                outputString += str(passenger.id) + ", "
            print("Bus %d has dropped off passengers %s at time %d" % (self.id, outputString, self.env.now))

# Set up graph for bus route
nodes = [1, 2, 3, 4, 5, 6, 7, 8]
edgeList = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 7), (7, 8), (8, 5)]
positions = [(0, 0), (0, 10), (0, 20), (30, 20), (30, 40), (40, 50), (50, 60), (30, 60), (50, 80), (80, 40)]
times = [5, 10, 7, 9, 8, 5, 6, 11, 6]
graph = nx.Graph()
graph.add_edges_from(edgeList)

#Reads in Passengers from CSV file
with open('Passenger.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader)
    passenger_list = []
    for row in reader:
        print(row)
        attribute = []
        [attribute.append(int(i)) for i in row[0].split(",")]
        
        passenger_list.append(Passenger(attribute[0], attribute[1], attribute[2]))

#PassengerList is a dictionary with all the passengers
passengerList = {}
for i in passenger_list:

    waiting_node = i.return_node()
    
    if waiting_node in passengerList.keys():

        passengerList[waiting_node].append(i)
    
    else:
        passengerList[waiting_node] = [i]

#Checks for empty nodes, if there are empty nodes, then fill them in with an empty list
for i in range(graph.number_of_nodes()+1):
    if i not in passengerList.keys():
        passengerList[i] = []

nx.set_node_attributes(graph, passengerList, 'passengers')

# Set the time needed to travel from one node to the next
i = 0
for (u, v) in edgeList:
    graph[u][v]['time'] = times[i]
    i += 1

# Visualize the graph
nx.draw_networkx(graph, positions, node_size=500, node_color='darkorange')  # draw graph
nx.draw_networkx_edge_labels(graph, positions,
                                     edge_labels=nx.get_edge_attributes(graph, 'times'))
plt.show()

# Create the simulation environment
env = simpy.Environment()

# Create the buses and routes
stopList1 = (1, 2, 3, 4, 5, 6)
bus1 = Bus(env, 1, 40, stopList1, graph)

stopList2 = (5, 7, 8)
bus2 = Bus(env, 2, 50, stopList2, graph)

# Run the simulation for a certain number of time steps
env.run(until=100)
