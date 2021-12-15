PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

adjacency_list = {}
paths = 0
paths_cache = {}

def increment_cache(path, passed_twice_through_small):
	path = path[:]
	while path:
		t = tuple(path)
		paths_cache[t] = paths_cache.get(t, 0) + 1

		v = path.pop()

def get_cache(path, passed_twice_through_small):
	t = tuple(path)
	return paths_cache.get(t, None)


def process(vertex):
	global adjacency_list, paths, paths_cache

	# DFS like approach, caching the number of paths for each path list
	queue = [[vertex, set(), False, []]]
	
	while queue:
		next = queue.pop()

		v = next[0]
		colored = next[1]
		passed_twice_through_small = next[2]
		path_so_far = next[3]

		if v == 'end':
			paths += 1
			increment_cache(path_so_far, passed_twice_through_small)
			continue
		elif v == 'start' and v in colored:
			continue

		if v.islower():
			if v in colored:
				if passed_twice_through_small:
					continue
				else:
					passed_twice_through_small = True
			else:
				# make deep copy so we don't change other sets
				colored = set(colored)
				colored.add(v)

		
		cached = get_cache(path_so_far, passed_twice_through_small)

		if cached is not None:
			paths += cached
			continue

		for conn in adjacency_list[v]:
			queue.append([conn, colored, passed_twice_through_small, path_so_far])


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