# Relation functions

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

def upper_negation(graph, subgraph):

    dual_graph = find_dual(graph)
    dual_subgraph = find_dual(subgraph)
    dual_negation = lower_negation(dual_graph, dual_subgraph)

    result = find_dual(dual_negation)

    return result


