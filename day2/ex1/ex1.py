PATH = 'ex1.txt'

with open(PATH) as f:
	lines = f.readlines()

position = [0, 0]
for line in lines:
	toks = line.split(' ')

	command = toks[0]
	distance = int(toks[1])

	if command == 'forward':
		position[0] += distance
	elif command == 'up':
		position[1] -= distance
	elif command == 'down':
		position[1] += distance

print(position[0] * position[1])