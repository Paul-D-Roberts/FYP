# Graph functions

def find_path():

    return None

def find_intersect(subgraph, subgraph2):

    subgraph_intersect = {x: subgraph[x] for x in subgraph if x in subgraph2}

    return subgraph_intersect

#
# def find_union(graph, subgraph, subgraph2):
#
#    subgraph_union = subgraph2.copy()
#    subgraph_union.update(subgraph)
#
#    if cmp(subgraph_union, graph) == 0:
#
#        return subgraph_union

def lower_negation(graph, subgraph):

    s1_nodes = set()
    s2_nodes = set()

    for k, v in subgraph[1].iteritems():
            for x in v:
                s1_nodes.add(x)

    for k, v in graph[1].iteritems():
        for x in v:
            if x not in s1_nodes:
                s2_nodes.add(x)

    return s2_nodes