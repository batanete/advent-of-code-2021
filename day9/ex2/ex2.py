PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

from functools import reduce
from sys import exit

largest_3_areas = []

def is_outside_border(matrix, pos):
	return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(matrix) or pos[1] >= len(matrix[0])

def draw_area(matrix, pos):
	colored = set()

	# using a BFS-like approach
	queue = [pos]
	while queue:
		next = queue.pop(0)

		if next in colored or is_outside_border(matrix, next) or int(matrix[next[0]][next[1]]) == 9:
			continue

		colored.add(next)

		queue.append((next[0] - 1, next[1]))
		queue.append((next[0] + 1, next[1]))
		queue.append((next[0], next[1] - 1))
		queue.append((next[0], next[1] + 1))
	return len(colored)

result = 0
for i, line in enumerate(lines):
	for j, point in enumerate(line):
		adjacent_points = []
		if j > 0 :
			adjacent_points.append(line[j - 1])
		if j < len(line) - 1:
			adjacent_points.append(line[j + 1])
		if i > 0 :
			adjacent_points.append(lines[i - 1][j])
		if i < len(lines) - 1:
			adjacent_points.append(lines[i + 1][j])

		if point < min(adjacent_points):
			# this is a low point
			area = draw_area(lines, (i, j))
			largest_3_areas.append(area)

			if len(largest_3_areas) > 3:
				largest_3_areas.remove(min(largest_3_areas))

print(reduce(lambda a,b: a * b, largest_3_areas))