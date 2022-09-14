# Importation of relevant packages
import matplotlib.pyplot as plt
import networkx as nx

# A Graph of a towns and their interconnections
icsb = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Sibiu': ['Fagara', 'RV']
}

# Creation of an empty graph using nx
ICS_Graph = nx.Graph()

# Looping through the graph to create the interconnected nodes
for node in icsb:
    for ne in icsb[node]:
        ICS_Graph.add_edge(node, ne, color='black')

# Positioning of nodes
x = nx.spring_layout(ICS_Graph)

# Addition of colours to the nodes of the graph
colors = [ICS_Graph[u][v]['color'] for u, v in ICS_Graph.edges()]
nx.draw(ICS_Graph, x, node_color='#ADD8E6', edge_color=colors, width=5, with_labels=True)

# Drawing the final graph
plt.show()
