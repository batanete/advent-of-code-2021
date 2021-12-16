PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

N_STEPS = 10

rules = {}
# using a char list to prevent unnecessary string instantiation when we insert chars
polymer = list(lines[0])

for line in lines[2:]:
	toks = line.split('->')

	pair = toks[0].strip()
	middle = toks[1].strip()

	rules[pair] = middle

for step in range(1, N_STEPS + 1):
	i = 1
	while i < len(polymer):
		pair = polymer[i - 1] + polymer[i]
		middle = rules[pair]
		polymer.insert(i, middle)
		i += 2

possible_elements = set()
for c in polymer:
	possible_elements.add(c)

counts = [polymer.count(c) for c in possible_elements]

print(max(counts) - min(counts))
