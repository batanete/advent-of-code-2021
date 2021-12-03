PATH = 'ex2.txt'

with open(PATH) as f:
	lines = f.readlines()

lines = [int(line) for line in lines]

count = 0
for i, line in enumerate(lines):
	current = sum(lines[i+1:i+4])
	previous = sum(lines[i:i+3])
	if current > previous:
		count += 1

print(count)