import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add two nodes
G.add_node(1)
G.add_node(2)

# Add an edge between the nodes
G.add_edge(1, 2)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', arrowstyle='->', arrowsize=20)
plt.show()
