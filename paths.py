# load the data in sparse matrix file format
import os
import pickle as pk

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + "/graphs"
pk_path = dir_path + "/pkfiles"


#loads a list with file names
filenames  = pk.load(open(pk_path + "/" + "names" + ".pkl", 'rb'))