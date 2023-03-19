import cookiemilk

################################################################################
# example data
cmap_student1 = [['A', 'B'], ['B', 'C'], ['C', 'D']]
cmap_student2 = [['F', 'B'], ['F', 'C'], ['F', 'E']]
cmap_student3 = [['A', 'G'], ['G', 'C'], ['G', 'D']]

student1 = cookiemilk.cmap2graph(cmap_student1, data_type='pair', read_from_file=False)
student2 = cookiemilk.cmap2graph(cmap_student2, data_type='pair', read_from_file=False)
student3 = cookiemilk.cmap2graph(cmap_student3, data_type='pair', read_from_file=False)

# arrange data
data = list([student1, student2, student3])

keyterms = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# average
average1 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=False, pfnet=True)
average2 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=4, pfnet=True)
average3 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=False, pfnet=False)

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(15, 5), dpi=100)

plt.subplot(231)
plt.title('Student1')
p1 = nx.draw(student1, with_labels=True)

plt.subplot(232)
plt.title('Student2')
nx.draw(student2, with_labels=True)

plt.subplot(233)
plt.title('Student3')
nx.draw(student3, with_labels=True)

plt.subplot(234)
plt.title('average PFNet')
nx.draw(average1, with_labels=True)

plt.subplot(235)
plt.title('average PFNet containing four most important terms')
nx.draw(average2, with_labels=True)

plt.subplot(236)
plt.title('weighted average graph')
pos = nx.spring_layout(average3, k=10)  # For better example looking
nx.draw(average3, pos, with_labels=True)
labels = {e: round(average3.edges[e]['weight'], 2) for e in average3.edges}
nx.draw_networkx_edge_labels(average3, pos, edge_labels=labels)

plt.savefig("four_grids.png")
plt.show()

nx.degree_centrality(average1)
