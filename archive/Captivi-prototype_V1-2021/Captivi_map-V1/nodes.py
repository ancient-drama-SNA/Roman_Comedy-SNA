import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# G.add_node("Tom")
# G.add_node("Jerry")

names1 = [("Hans", "Nate"), 
         ("Hans", "Ross"), 
         ("Hans", "Kent"), 
         ("Hans", "Dustin"),
         ("Hans", "John")]

names2 = [("Nate", "Ross"),
          ("Nate", "Mark"),
          ("Nate", "Dustin"),
          ("Nate", "Karl")]

names3 = [("Ross", "Nate"),
          ("Ross", "Karl"),
          ("Ross", "Kent"),
          ("Ross", "Mike")]


# G.add_edge("Tom", "Jerry")
G.add_edge("Nate", "Ed")

G.add_edges_from(names1) 
G.add_edges_from(names2) 
G.add_edges_from(names3)

nx.draw(G, with_labels=True, font_size=12, font_family = "elena", bbox=dict())
plt.show()
