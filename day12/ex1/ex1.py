PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

colored_vertexes = set()
adjacency_list = {}
paths = 0
def process(vertex):
	global adjacency_list, colored_vertexes, paths

	if vertex == 'end':
		paths += 1
		return

	if vertex.islower():
		colored_vertexes.add(vertex)

	connections = [v for v in adjacency_list.get(vertex, []) if v not in colored_vertexes]

	for connection in connections:
		process(connection)

	colored_vertexes.discard(vertex)


for line in lines:
	toks = line.split('-')
	source = toks[0]
	destination = toks[1]

	if source not in adjacency_list.keys():
		adjacency_list[source] = [destination]
	else:
		adjacency_list[source].append(destination)

	if destination not in adjacency_list.keys():
		adjacency_list[destination] = [source]
	else:
		adjacency_list[destination].append(source)

process('start')
print(paths)