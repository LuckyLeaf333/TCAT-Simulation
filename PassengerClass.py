class Passenger:
    def __init__(self, w_node, node_traveled):
        self.w_node = w_node
        self.node_traveled = node_traveled

    def update(self):
        self.node_traveled -= 1
        return (self.node_traveled)


# def on_bus(): #returns true if a specific passenger is on a specific bus
#         if self.bus.currentpass.contains(Passenger):
#             return true

# a = Passenger(1,2)
