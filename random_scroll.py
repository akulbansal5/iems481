import random


def randomScroll(coords, order):

    covered_nodes = []
    matching = []

    for i in order:
        edge = coords[i]
        nodea = edge[0]
        nodeb = edge[1]
        if nodea not in covered_nodes and nodeb not in covered_nodes:
            matching.append(edge)
            covered_nodes.append(nodea)
            covered_nodes.append(nodeb)
    
    return matching

def random_main(coords, iterations):

    bestOrder = None
    
    m = len(coords)                     #number of edges
    bestLen = 0

    for i in range(iterations):

        order = list(range(m))
        random.shuffle(order)
        # print(order)

        matching = randomScroll(coords, order)
        m_len = len(matching)
        if m_len > bestLen:
            bestLen = m_len
            bestOrder = order.copy()
        print("iteration", i)
    best_matching = randomScroll(coords, bestOrder)
    print("---------")

    return best_matching, len(best_matching)





