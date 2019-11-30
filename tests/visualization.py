import networkx as nx
from nagi.neat import Genome
from nagi.visualization import get_node_coordinates
from itertools import count
import matplotlib.pyplot as plt

input_size = 3
output_size = 5
test_genome = Genome(0, input_size, output_size, count(input_size + output_size + 1), is_initial_genome=True)
for i in range(10):
    test_genome.mutate()

    nodes = [key for key in test_genome.nodes.keys()]
    node_color = ['b' if node < input_size else 'r' if node < input_size+output_size else 'g' for node in nodes]

    edges = [(connection.origin_node, connection.destination_node) for connection in test_genome.connections.values()]

    g = nx.DiGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    pos = get_node_coordinates(test_genome)
    nx.draw_networkx(g, pos=pos, with_labels=True, nodes=nodes, node_color=node_color, font_color="w")
    plt.show()