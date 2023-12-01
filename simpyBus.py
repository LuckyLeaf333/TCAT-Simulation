import simpy
import matplotlib.pyplot as plt
import networkx as nx


class Passenger:
    def __init__(self, id, start, target):
        self.id = id
        self.target = target
        self.start = start

class Bus(object):
    """
    env: Simpy environment
    id: Id number for the bus (integer)
    stopList: list of the names of stops, the nodes the bus stops at
    travelTimes: travelTimes[a] is the time needed to travel from stopList[a] to stopList[a + 1].
                    If the stop is the last stop in the list, it is the time from stopList[a] to stopList[0]
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

    def nextStopIndex(self):
        if self.stopIndex == len(self.stopList) - 1:
            return 0
        return self.stopIndex + 1

    def run(self):
        while True:
            # Travel to next stop
            nextStopName = self.stopList[self.nextStopIndex()]
            yield self.env.process(self.goToNextStop(graph[self.stopName][nextStopName]['time']))

            # Board passengers if bus not full
            if self.numPassengers < self.capacity:
                yield self.env.process(self.pickUpPassengers(5))
            print("Bus %d is leaving stop %s at time %d" % (self.id, self.stopName, self.env.now))

    def goToNextStop(self, duration):
        yield self.env.timeout(duration)
        self.stopIndex = self.nextStopIndex()
        self.stopName = self.stopList[self.stopIndex]
        print("Bus %d has arrived at stop %s at time %d" % (self.id, self.stopName, self.env.now))

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


# Set up graph for bus route
nodes = [1, 2, 3, 4, 5, 6, 7, 8]
edgeList = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 7), (7, 8), (8, 5)]
positions = [(0, 0), (0, 10), (0, 20), (30, 20), (30, 40), (40, 50), (50, 60), (30, 60), (50, 80), (80, 40)]
times = [5, 10, 7, 9, 8, 5, 6, 11, 6]
graph = nx.Graph()
graph.add_edges_from(edgeList)

passengerList = {1: [Passenger(1, 1, 5), Passenger(2, 1, 1)], 2: [], 3: [], 4:[], 5:[Passenger(3, 5, 8), Passenger(4, 5, 1)],
                 6:[], 7:[], 8:[]}
nx.set_node_attributes(graph, passengerList, 'passengers')

i = 0
for (u, v) in edgeList:
    graph[u][v]['time'] = times[i]
    i += 1

nx.draw_networkx(graph, positions, node_size=500, node_color='darkorange')  # draw graph
nx.draw_networkx_edge_labels(graph, positions,
                                     edge_labels=nx.get_edge_attributes(graph, 'times'))
plt.show()

env = simpy.Environment()

stopList1 = (1, 2, 3, 4, 5, 6)
bus1 = Bus(env, 1, 40, stopList1, graph)

stopList2 = (5, 7, 8)
bus2 = Bus(env, 2, 50, stopList2, graph)

env.run(until=100)
