from venv import create
import gurobipy as gp
from gurobipy import GRB

"""
an optimization model for determining the max cardinality matching
"""

def createNodeDict(coords):

    nodeDict = {}

    for edge in coords:
        
        if edge[0] not in nodeDict:
            nodeDict[edge[0]] = []
        if edge[1] not in nodeDict:
            nodeDict[edge[1]] = []
        nodeDict[edge[0]].append(edge)
        nodeDict[edge[1]].append(edge)

    return nodeDict

def declare_variables(coords, model):

    x = model.addVars(coords, vtype = GRB.BINARY, obj = 1, name = 'x')

    return x

def declare_constraints(coords, x, node_dict, model):
    
    """
    declare the constraint in the problem
    """

    for node in node_dict:

        node_edges = node_dict[node]
        expr = gp.quicksum([x[edge[0], edge[1]] for edge in node_edges])
        model.addConstr(expr <= 1, name = f"node{node}")
    
def matching_solver(coords, iterations = None):
    
    """
    finds the maxima
    """

    model = gp.Model("matching")
    x = declare_variables(coords, model)
    node_dict = createNodeDict(coords)
    declare_constraints(coords, x, node_dict, model)
    model.write("matching.lp")
    model.setObjective(x.sum(), GRB.MAXIMIZE)
    model.optimize()

    if model.SolCount > 0:
        return "sol", model.ObjVal
    
    return "sol", -1






