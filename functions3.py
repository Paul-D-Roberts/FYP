# Relation functions

def find_dual(relation):

	relation_dual = [relation[0], {}]

	for edge, node in relation[1].iteritems():
			for element in node:
				keys = relation_dual[1].setdefault(element, [])
				keys.append(edge)
	return relation_dual

