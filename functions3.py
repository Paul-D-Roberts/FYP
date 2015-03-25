# Relation functions
import copy

def find_dual(relation):

    relation_dual = [relation[0], {}]

    for edge, node in relation[1].iteritems():
            for element in node:
                keys = relation_dual[1].setdefault(element, [])
                keys.append(edge)
    return relation_dual

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

def union(subgraph, subgraph2):

    subgraph_union = [set(), {}]

    nodes = subgraph[0].union(subgraph2[0])
    subgraph_edges = subgraph[1]
    subgraph2_edges = subgraph2[1]
    subgraph_union[0].update(nodes)
    subgraph_union[1].update(subgraph_edges)
    subgraph_union[1].update(subgraph2_edges)

    return subgraph_union

def intersect(subgraph, subgraph2):

    subgraph_intersect = [set(), {}]

    nodes = subgraph[0].intersection(subgraph2[0])
    edges = {x: subgraph[1][x] for x in subgraph[1] if x in subgraph2[1]}

    subgraph_intersect[0].update(nodes)
    subgraph_intersect[1].update(edges)

    return subgraph_intersect

def complement(graph, subgraph):

    graph_complement = copy.deepcopy(graph)

    graph_complement[0].difference_update(subgraph[0])

    for key2 in subgraph[1]:
        for key1 in graph[1]:
            if key1 == key2:
                del graph_complement[1][key1]
            else:
                values = graph_complement[1][key1]
                if key2 in values:
                    values.remove(key2)

    return graph_complement


def find_upper_negation(graph, subgraph):

    graph_complement = complement(graph, subgraph)
    complement_dual = find_dual(graph_complement)
    dual_negation = lower_negation(graph_complement, complement_dual)
    upper_negation = complement(graph, dual_negation)

    return upper_negation