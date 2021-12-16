PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

matrix = []
border_x = 0
border_y = 0

def insert_lazy(x, y):
	global border_x, border_y

	while len(matrix) < y + 1:
		matrix.append([])
	while len(matrix[y]) < x + 1:
		matrix[y].append(False)

	border_x = max(border_x, x)
	border_y = max(border_y, y)

	matrix[y][x] = True

def get_lazy(x, y):
	if len(matrix) < y + 1 or len(matrix[y]) < x + 1:
		return False

	return matrix[y][x]

def fold(axis, line):
	global border_y, border_x

	if axis == 'y':
		for x in range(0, border_x + 1):
			for y in range(line, border_y + 1):
				symmetric_y = line - (y - line)
				if symmetric_y < 0:
					break
				if get_lazy(x, y):
					insert_lazy(x, symmetric_y)

		border_y = line
	else:
		for x in range(line, border_x + 1):
			symmetric_x = line - (x - line)
			if symmetric_x < 0:
				break
			for y in range(0, border_y + 1):
				if get_lazy(x, y):
					insert_lazy(symmetric_x, y)

		border_x = line


def count_dots():
	global matrix

	count = 0
	for row in matrix[:border_y + 1]:
		count += row[:border_x + 1].count(True)

	return count

def print_to_file():
	with open('out.txt', 'w') as f:
		for y in range(border_y + 1):
			for x in range(border_x):
				f.write('#' if get_lazy(x, y) else '.')
			f.write('\n')


# read dots
ind = 0
for line in lines:
	ind += 1

	if len(line) == 0:
		break

	toks = line.split(',')
	x, y = int(toks[0]), int(toks[1])
	insert_lazy(x, y)

# read folds
for line in lines[ind:]:
	last_tok = line.split(' ')[-1]
	toks = last_tok.split('=')
	axis = toks[0]
	line = int(toks[1])
	fold(axis, line)

print(count_dots())
print_to_file()