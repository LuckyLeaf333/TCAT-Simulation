import simpy


class Bus(object):
    """
    env: Simpy environment
    id: Id number for the bus (integer)
    stopList: list of the names of stops, the nodes the bus stops at
    travelTimes: travelTimes[a] is the time needed to travel from stopList[a] to stopList[a + 1].
                    If the stop is the last stop in the list, it is the time from stopList[a] to stopList[0]
    """
    def __init__(self, env, id, capacity, stopList, travelTimes):
        self.env = env
        self.id = id
        self.capacity = capacity
        self.stopList = stopList
        self.travelTimes = travelTimes
        self.stopIndex = 0
        self.stopName = self.stopList[self.stopIndex]

        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def nextStopIndex(self):
        if self.stopIndex == len(self.stopList) - 1:
            return 0
        return self.stopIndex + 1

    def run(self):
        while True:
            # Travel to next stop
            yield self.env.process(self.goToNextStop(self.travelTimes[self.stopIndex]))

            # Check if there are passengers to board

    def goToNextStop(self, duration):
        print("Bus %d is leaving stop: %s at time %d" % (self.id, self.stopList[self.stopIndex], self.env.now))
        yield self.env.timeout(duration)
        self.stopIndex = self.nextStopIndex()
        self.stopName = self.stopList[self.stopIndex]
        print("Bus %d has arrived at stop: %s at time %d" % (self.id, self.stopList[self.stopIndex], self.env.now))


env = simpy.Environment()

stopList = ("Stop 1", "Stop 2", "Stop 3", "Stop 4")
travelTimes = (5, 7, 8, 9)
# stores amount of time need to go from stop at current index to next index

stopList2 = ("Stop A", "Stop B", "Stop C", "Stop D")
travelTimes2 = (10, 5, 9, 8)

bus1 = Bus(env, 1, 40, stopList, travelTimes)
bus2 = Bus(env, 2, 30, stopList2, travelTimes2)

env.run(until=40)
