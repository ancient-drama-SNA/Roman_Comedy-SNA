'''
Simple script for mapping SNA data.
'''

import networkx as nx
import matplotlib.pyplot as plt
import xlrd

file = "Captivi.xls"

G = nx.Graph()

names = []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(0)

for row in range(sheet.nrows):
    data = sheet.row_slice(row)
    person1 = data[0].value
    person2 = data[1].value
    names.append((person1, person2))

G.add_edges_from(names)
print(names)
nx.draw(G, with_labels=True, font_size=12, font_family = "elena", bbox=dict())

plt.show()
