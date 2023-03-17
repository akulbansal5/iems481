import os
import networkx as nx
import pickle as pk
import matplotlib.pyplot as plt


"""
finds the max cardinality matching and also plots it

"""

# load the data in sparse matrix file format
dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + "/graphs"
pk_path = dir_path + "/pkfiles"


#loads a list with file names
filenames  = pk.load(open(pk_path + "/" + "names" + ".pkl", 'rb'))

#loads a particular file
file_path = pk_path + "/" + filenames[13] + ".pkl"
file_coords = pk.load(open(file_path, 'rb'))

print(file_coords)


G = nx.Graph(file_coords)
best_matching = sorted(nx.max_weight_matching(G, maxcardinality= True))
print(f"len of max match: {len(best_matching)}, total edges: {len(file_coords)}")
all_edges = G.edges()
color = []
for edge in all_edges:
    rev_edge = (edge[1], edge[0])
    if edge in best_matching or rev_edge in best_matching:
        color.append(0.9)
    else:
        color.append(0.1)

nx.draw_networkx(G, arrows = True, edge_color = color, arrowstyle = '-')

print("best matching: ", best_matching)
plt.show()





