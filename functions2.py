# Graph functions

def validity_check(graph):

    valid = True

    for key, value in graph[1].iteritems():
        if not value:
            valid = False
            print('Edge connected to no nodes')
            break

        else:
            for x in value:
                if x not in graph[0]:
                    print('Graph contains reference to invalid node')
                    valid = False
                    break
    return valid

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

    subgraph_nodes = set()
    deleted_nodes = set()
    subgraph3 = [set(), {}]

    for keys, values in subgraph[1].iteritems():
        for element in values:
                subgraph_nodes.add(element)

    for keys, values in graph[1].iteritems():
        for element in values:
            if element in subgraph_nodes:
                deleted_nodes.add(element)
            else:
                subgraph3[0].add(element)

    for keys, values in graph[1].iteritems():
        for elements in values:
            if elements in deleted_nodes:
                break
        else:
            subgraph3[1][keys] = values

    return subgraph3

