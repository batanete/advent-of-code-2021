from math import sqrt

PATH = 'ex1.txt'

SIZE_MATRIX = 10000
with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

# this is better than list of lists(more memory efficient)
matrix = {}
n_marked_with_two = 0

n_marked_with_two = 0

def is_vertical(line):
	return line[0][0] == line[1][0]

def is_horizontal(line):
	return line[0][1] == line[1][1]

def get_direction(line):
	p1, p2 = line[0], line[1]

	if is_horizontal(line):
		return (1 if p2[0] - p1[0] > 0 else -1, 0)
	else:
		return (0, 1 if p2[1] - p1[1] > 0 else -1)


def mark(line):
	global n_marked_with_two

	direction = get_direction(line)

	current = line[0][:]
	while True:
		current_tuple = tuple(current)

		times_marked = matrix.get(current_tuple, 0) + 1
		matrix[current_tuple] = times_marked

		if times_marked == 2:
			n_marked_with_two += 1

		if current == line[1]:
			break
		
		current[0] += direction[0]
		current[1] += direction[1]


for l in lines:
	points = [tok.strip().split(',') for tok in l.split("->")]
	line = [int(i) for i in points[0]], [int(i) for i in points[1]]

	if is_vertical(line) or is_horizontal(line):
		mark(line)

print(n_marked_with_two)