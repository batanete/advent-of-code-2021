PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

points_by_char = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

closing_to_opening_chars = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
}

def process(line):
	stack = []

	for c in line:
		if c in closing_to_opening_chars.values():
			stack.append(c)
		else:
			if not stack or stack.pop() != closing_to_opening_chars[c]:
				return points_by_char[c]

	return 0

result = 0
for line in lines:
	result += process(line)

print(result)