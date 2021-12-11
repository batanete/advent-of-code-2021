PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

points = []

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
			result += int(point) + 1	

print(result)