import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("Tom")
G.add_node("Jerry")

G2 = nx.Graph()
G2.add_node("Betty")
G2.add_node("Lucy")

plt.figure(1)
nx.draw(G)

plt.figure(2)
nx.draw(G2, node_color="red")

plt.show()
