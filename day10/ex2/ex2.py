PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

points_by_char = {
	'(': 1,
	'[': 2,
	'{': 3,
	'<': 4,
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
			# invalid line
			if not stack or stack.pop() != closing_to_opening_chars[c]:
				return None

	points = 0
	for c in stack[::-1]:
		points = points * 5 + points_by_char[c]

	return points

results = []
for line in lines:
	result = process(line)
	if result is not None:
		results.append(result)

list.sort(results)
result = results[len(results) // 2]	

print(result)