from math import sqrt

PATH = 'ex2.txt'

SIZE_MATRIX = 10000
with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

# could be done with numpy arrays for better performance
matrix = []
for i in range(SIZE_MATRIX):
	matrix.append([0] * SIZE_MATRIX)

n_marked_with_two = 0

def is_vertical(line):
	return line[0][0] == line[1][0]

def is_horizontal(line):
	return line[0][1] == line[1][1]

def get_direction(line):
	p1, p2 = line[0], line[1]

	diff1 = p2[0] - p1[0]
	diff2 = p2[1] - p1[1]

	return (
		1 if diff1 > 0 else (0 if diff1 == 0 else - 1),
		1 if diff2 > 0 else (0 if diff2 == 0 else - 1)
	)


def mark(line):
	global n_marked_with_two

	direction = get_direction(line)
	print(line, direction)

	current = line[0][:]
	while True:

		matrix[current[1]][current[0]] += 1
		times_marked = matrix[current[1]][current[0]]

		if times_marked == 2:
			n_marked_with_two += 1

		if current == line[1]:
			break
		
		current[0] += direction[0]
		current[1] += direction[1]


for l in lines:
	points = [tok.strip().split(',') for tok in l.split("->")]
	line = [int(i) for i in points[0]], [int(i) for i in points[1]]

	mark(line)

print(n_marked_with_two)