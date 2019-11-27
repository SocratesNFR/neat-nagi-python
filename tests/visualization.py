import networkx as nx
from nagi.neat import Genome
from itertools import count
import matplotlib.pyplot as plt

test_genome = Genome(0, 3, 2, count(0), is_initial_genome=True)
# for i in range(10):
#     test_genome.mutate()
pos = {0: [0, 2],
       1: [0, 1],
       2: [0, 0],
       3: [1, 0.5],
       4: [1, 1.5]}

nodes = [key for key in test_genome.nodes.keys()]
node_color = ['b' if node < 3 else 'r' if node < 5 else 'g' for node in nodes]

edges = [(connection.in_node, connection.out_node) for connection in test_genome.connections.values()]

g = nx.DiGraph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)

nx.draw_networkx(g, pos=pos, with_labels=True, nodes=nodes, node_color=node_color, font_color="w")
plt.show()
