PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

matrix = []

for line in lines:
	matrix.append([int(i) for i in line])

end = (len(matrix) - 1, len(matrix[0]) - 1)
best_path = None
best_path_by_position = {}
min_risk_on_enter_position = {}
heuristic_cache = {}

def get(x, y):
	if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
		# out of bounds
		return None
	return matrix[y][x]

def heuristic(x, y):
	cached = heuristic_cache.get((x, y), None)

	if cached is not None:
		return cached

	# the best path from (x, y) to end always has less or equal risk
	# than the one taken by going all the way down and then right
	result = 0
	while x < len(matrix[0]) - 1:
		result += matrix[y][x]
		x += 1

	while y < len(matrix):
		result += matrix[y][x]
		y += 1

	heuristic_cache[(x, y)] = result
	return result

def is_feasible(x, y, risk_before):
	global best_path, best_path_by_position, best_path_in_pos, min_risk_on_enter_position
	risk = risk_before + get(x, y)

	if risk + (end[0] - x + end[1] - y) > best_path:
		return False

	min_risk = min_risk_on_enter_position.get((x, y), None)

	if min_risk is None or min_risk > risk_before:
		min_risk_on_enter_position[(x, y)] = risk_before
	else:
		return False

	best_path_by_position[(x, y)] = best_path_by_position.get((x, y), risk_before + heuristic(x, y))
	best_path_in_pos = best_path_by_position[(x, y)]

	if best_path > best_path_in_pos:
		best_path = best_path_in_pos
	
	return best_path > risk

def mark_best_path(path, risk):
	while path:
		pos = path.pop()
		best_path_by_position[pos] = risk

best_path = heuristic(0, 0)
queue = [[(0, 0), 0, []]]
while queue:
	next = queue.pop()
	x, y = next[0]
	risk_before = next[1]
	path_so_far = next[2][:]

	node_risk = get(x, y)
	if node_risk is None:
		continue

	path_so_far.append((x, y))
	risk = risk_before + node_risk

	if (x, y) == end:
		if best_path > risk:
			best_path = risk
			mark_best_path(path_so_far, risk)
			continue
	elif not is_feasible(x, y, risk_before):
		continue

	connections = [
		(x + 1, y),
		(x - 1, y),
		(x, y + 1),
		(x, y - 1),
	]

	for conn in connections:
		queue.append([conn, risk, path_so_far])

# dont count risk for entrance
best_path -= get(0, 0)
print(best_path)
