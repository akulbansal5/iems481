from scipy.io import mmread
import os
import numpy as np
import pickle as pk

"""
loads the data from sparse matrix file format and dumps them into pk files
Each pk file contains a list of edges in the graph
"""

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + "/graphs"
pk_path = dir_path + "/pkfiles"

def filterduplicates(coords):

    #deletes the loops from list of coordinates (list of tuples)
    # for instance (0,1) and (1, 0) can not both be there
    #returns the duplicates that are in the file

    store = {}
    out = []

    for coo in coords:

        if store.get(coo[1], -1) == -1:                  #not in the list
            if store.get(coo[0], -1) == -1:
                store[coo[0]] = {}
                store[coo[0]][coo[1]] = 1
            elif store[coo[0]].get(coo[1], -1) == -1:
                store[coo[0]][coo[1]] = 1
            out.append(coo)
        elif store[coo[1]].get(coo[0], -1) == -1:        #not in sublist
            if store.get(coo[0], -1) == -1:
                store[coo[0]] = {}
                store[coo[0]][coo[1]] = 1
            elif store[coo[0]].get(coo[1], -1) == -1:
                store[coo[0]][coo[1]] = 1
            out.append(coo)
    
    return out
            

        

                
                





def filterloops(coords):

    #filters the self loops or coordinates of type (x, x)

    coords = coords.copy()
    ind = 0
    
    while ind < len(coords):
        if coords[ind][0] == coords[ind][1]:
            del coords[ind]
        else:
            ind += 1
    
    return coords


#loops over all files in the folder
filenames = []
iter = 0
for subdir, dirs, files in os.walk(data_path):
    
    
    for file in files:
        
        if file[-3:] == "mtx":
            mtx_file_path = os.path.join(subdir, file)
            mat_coo = mmread(f"{mtx_file_path}")
            if type(mat_coo).__module__ != np.__name__:
                filename = file[:-4]
                
                
                coords = list(zip(mat_coo.row, mat_coo.col))
                print(f"---iter: {iter}, coords_len originally: {len(coords)}  ---")
                # print(f"coords before removing loops: {len(coords)}")
                coords = filterloops(coords)           #filter self-loops from the data
                print(f"---iter: {iter}, coords_len after removing loops: {len(coords)}  ---")

                coords = filterduplicates(coords)
                print(f"---iter: {iter}, coords_len after removing duplicates: {len(coords)}  ---")

                iter += 1


                #dump the data
                if len(coords) > 0:
                    
                    
                    # print("row", mat_coo.row)
                    # print("col", mat_coo.col)


                    with open(pk_path + "/" + filename + ".pkl", 'wb') as f:
                        pk.dump(coords, f)
                    filenames.append(filename)

                    with open(pk_path + "/" + filename + ".txt", 'w') as g:
                        for edge in coords:
                            g.writelines(str(edge))
                            g.write("\n")         

                else:
                    print(f"the following file is deleted: {filename}")


with open(pk_path + "/" + "names" + ".pkl", 'wb') as f:
    pk.dump(filenames, f)








