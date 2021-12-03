PATH = 'ex1.txt'

with open(PATH) as f:
	lines = f.readlines()

count = 0
for i, line in enumerate(lines[1:]):
	previous = int(lines[i])
	if (int(line) > previous):
		count += 1

print(count)