PATH = 'ex2.txt'
from sys import exit

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

first_tile = []

for line in lines:
	first_tile.append([int(i) for i in line])

matrix = []

for i in range(5):
	for row in first_tile:
		matrix.append([])
		for j in range(5):
			for n in row:
				el = (n + i + j)
				if el > 9:
					el = el % 10 + 1
				matrix[-1].append(el)

end = (len(matrix) - 1, len(matrix[0]) - 1)
best_path = None

best_path_by_position = {}
min_risk_on_enter_position = {}
best_path_by_position = {}
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

	# optimization: the best path from (x, y) to end always has less or equal risk
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
	global best_path, min_risk_on_enter_position, best_path_by_position

	risk = risk_before + get(x, y)

	# optimization: the best possible path from (x, x) to end, is the one
	# we get if we assume we always go right and down and all squares are one.
	if risk + (end[0] - x + end[1] - y) > best_path:
		return False

	# optimization: if we entered this node previously with less distance traversed
	# then we can discard this path
	min_risk = min_risk_on_enter_position.get((x, y), float('Inf'))

	if min_risk > risk_before:
		min_risk_on_enter_position[(x, y)] = risk_before
	else:
		return False

	# optimization: if the best path obtained from this node is better than our current risk
	# ammount, we can discard this path
	best_path_by_position[(x, y)] = best_path_by_position.get((x, y), risk_before + heuristic(x, y))
	best_path_in_pos = best_path_by_position[(x, y)]

	if best_path > best_path_in_pos:
		best_path = best_path_in_pos

	return best_path > risk


best_path = heuristic(0, 0)
stack = [[(0, 0), 0, []]]
while stack:
	next = stack.pop()
	x, y = next[0]
	risk_before = next[1]

	node_risk = get(x, y)

	# out of bounds
	if node_risk is None:
		continue

	risk = node_risk + risk_before

	if not is_feasible(x, y, risk_before):
		continue

	elif (x, y) == end:
		if best_path is None or best_path > risk:
			best_path = risk
			continue

	connections = [
		(x + 1, y),
		(x, y - 1),
		(x - 1, y),
		(x, y + 1),
	]

	for conn in connections:
		stack.append([conn, risk])

# dont count risk for entrance
best_path -= get(0, 0)
print(best_path)
