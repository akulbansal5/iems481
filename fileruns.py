"""
a general code for running all the files with a particular algorithm
two main algorithms are coded so far: 

random_main: does a random shuffle of the data and applies the greedy algorithm
matching_solver: gurobi optimization model for finding the max cardinality matching
"""


# import os
# from random import random
# import networkx as nx
import pickle as pk
import csv
# import matplotlib.pyplot as plt
from random_scroll import random_main
# from gurobi_model import matching_solver
from paths import filenames, pk_path

#loads a particular file
# file_path = pk_path + "/" + filenames[13] + ".pkl"
# file_coords = pk.load(open(file_path, 'rb'))


# G = nx.Graph()
# G.add_edges_from(file_coords)
# all_edges = G.edges()
# best_matching = sorted(nx.max_weight_matching(G, maxcardinality= True))


# matching, m_len = random_main(file_coords, iterations = 10)


def algo_run(algo_name, filenames, name = "default", outfile = "matching_new.csv"):

    with open(outfile, mode = 'w+') as ex1file:

        fieldnames = ["algoname", "filename", "max_matching", "total_edges"]
        writer = csv.writer(ex1file)
        writer.writerow(fieldnames)

    for i in range(len(filenames)):
        file_path = pk_path + "/" + filenames[i] + ".pkl"
        file_coords = pk.load(open(file_path, 'rb'))
        matching, m_len = algo_name(file_coords, iterations = 1)

        print(f"file: {filenames[i]}, len of matching: {m_len}, len of corrds: {len(file_coords)}")
    
        with open(outfile, mode = 'a+') as ex1file:

            fieldnames = [name, filenames[i],m_len, len(file_coords)]
            writer = csv.writer(ex1file)
            writer.writerow(fieldnames)
    
            




algo_run(random_main, filenames)

# algo_run(matching_solver, filenames, name= "opt", outfile="match_opt.csv")
# print(f"len of proposed matching: {len(matching)}")
# print(f"length of maximum matching: {len(best_matching)}")
# print(f"total number of edges: {len(all_edges)}")
