"""
Homework 1 on degree distributions
"""
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}
EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
def make_complete_graph(num_nodes):
    """
    Computes a complete graph for num_nodes number of nodes
    :param num_nodes:
    :return: dgraph
    """
    #A list comprehension inside the dict comprehension generates all possible nodes for any
    #Given key(e.g. node)
    if num_nodes > 0:
        dgraph = {key: set([val for val in range(0,num_nodes) if val !=key]) for key in range(0,num_nodes)}
    else:
        dgraph = {}
    return dgraph

def compute_in_degrees(digraph):
    """
    Computes the in-degrees for each node in provided graph rep (drected graph)
    """
    degrees_count = {key:0 for key in digraph}
    for key in digraph:
        for outs in digraph[key]:
            degrees_count[outs] += 1

    return degrees_count

def in_degree_distribution(digraph):
    """
    Computes the distribution of in-degrees for our graph
    :param digraph:
    :return:
    """
    computed_in_degree = compute_in_degrees(digraph)
    in_distribution = dict()
    for dummy_key, value in computed_in_degree.iteritems():
        if value in in_distribution:
            in_distribution[value] += 1
        else:
            in_distribution[value] = 1
    return  in_distribution

def normalized_distribution(digraph):
    """
    Takes a graph & returns the normalized distribution
    :param digraph:
    :return:
    """
    indeg = in_degree_distribution(digraph)
    sum_occur = 0
    for dummy_key,value in indeg.iteritems():
        sum_occur += value
    for key,value in indeg.iteritems():
        indeg[key] = (float(value)/float(sum_occur))
    return  indeg

