
def find_path(graph,start,end,path=[]):
	path = path + [start]
	
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			new_path = find_path(graph,node,end,path)
			if new_path: 
				return new_path
	return None

def union (graph,graph2):
	graphUnion = graph2.copy()
	graphUnion.update(graph)
	
	return graphUnion
	
def intersect (subgraph,subgraph2):
	subgraphIntersect = {x:subgraph[x] for x in subgraph if x in subgraph2}
	
	return subgraphIntersect
	

#def lower_negation(graph,graph2)
