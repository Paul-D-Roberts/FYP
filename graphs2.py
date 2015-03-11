# Improved graph structure to support multiple edges
# to the same node and enable edge labelling

G = [[1, 2, 3], {'A': [1, 2], 'B': [2, 3]}]

subG = [[1, 2], {'A': [1, 2]}]


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