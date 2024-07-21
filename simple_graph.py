import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.MultiDiGraph()

# Add a single node
G.add_node("A")

# Draw the graph
nx.draw(G, with_labels=True, node_color="lightblue")

# Save the graph as a PNG file
plt.savefig("graph.png")
plt.show()
