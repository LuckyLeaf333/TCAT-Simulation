class Passenger:
    def __init__(self, w_node, node_traveled):
        self.w_node = w_node
        self.node_traveled = node_traveled

    def update(self):
        self.node_traveled -= 1
        return (self.node_traveled)



