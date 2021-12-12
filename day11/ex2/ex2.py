PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

REQUIRED_FLASHES = len(lines) * len(lines[0])
matrix = []
flashed_in_step = set()

def is_outside_border(pos):
	return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(matrix) or pos[1] >= len(matrix[0])

def process(i, j):
	global flashes, flashed_in_step, matrix
	# bfs-like approach
	queue = [(i, j)]

	while queue:
		next = queue.pop(0)
		if is_outside_border(next) or next in flashed_in_step:
			continue

		new_value = matrix[next[0]][next[1]] + 1
		if new_value <= 9:
			matrix[next[0]][next[1]] = new_value
			continue

		# flash occurred, propagate it
		flashed_in_step.add(next)
		matrix[next[0]][next[1]] = 0

		queue.append((next[0] + 1, next[1] + 1))
		queue.append((next[0] - 1, next[1] - 1))
		queue.append((next[0] + 1, next[1] - 1))
		queue.append((next[0] - 1, next[1] + 1))

		queue.append((next[0] - 1, next[1]))
		queue.append((next[0] + 1, next[1]))
		queue.append((next[0], next[1] - 1))
		queue.append((next[0], next[1] + 1))



for line in lines:
	matrix.append([int(c) for c in line])

step = 0
while len(flashed_in_step) != REQUIRED_FLASHES:
	step += 1
	flashed_in_step = set()
	for i, row in enumerate(matrix):
		for j, octupus in enumerate(row):
			process(i, j)

print(step)