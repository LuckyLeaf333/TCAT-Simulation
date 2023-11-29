import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 11))
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)])
    return G

def visualize_graph(G, pos=None):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=8, font_color='black', font_weight='bold')
    plt.show()

def simulate_bus(graph, bus_speed=1):
    pos = nx.spring_layout(graph)
    visualize_graph(graph, pos)

    bus_node = random.choice(list(graph.nodes()))
    while True:
        next_node = random.choice(list(graph.neighbors(bus_node)))
        print(f"Bus moving from Node {bus_node} to Node {next_node}")
        time.sleep(bus_speed)

        passengers = random.randint(0, 5)
        print(f"Bus picking up {passengers} passengers at Node {next_node}")

        bus_node = next_node

        visualize_graph(graph, pos)

simulate_bus(create_graph())