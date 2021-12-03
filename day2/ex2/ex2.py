PATH = 'ex2.txt'

with open(PATH) as f:
	lines = f.readlines()

aim = 0
position = [0, 0]
for line in lines:
	toks = line.split(' ')

	command = toks[0]
	amount = int(toks[1])

	if command == 'forward':
		position[0] += amount
		position[1] += amount * aim
	elif command == 'up':
		aim -= amount
	elif command == 'down':
		aim += amount

print(position[0] * position[1])