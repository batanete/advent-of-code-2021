PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

N_STEPS = 40

rules = {}
polymer = lines[0]


for line in lines[2:]:
	toks = line.split('->')

	pair = toks[0].strip()
	middle = toks[1].strip()

	rules[pair] = middle

pair_occurrences = {}
occurrences = {}
for i, c in enumerate(polymer[:-1]):
	pair = c + polymer[i + 1]
	pair_occurrences[pair] = pair_occurrences.get(pair, 0) + 1
	occurrences[c] = occurrences.get(c, 0) + 1

occurrences[polymer[-1]] = occurrences.get(polymer[-1], 0) + 1

for step in range(1, N_STEPS + 1):
	new_occurences = {}
	for pair, count in pair_occurrences.items():
		middle = rules[pair]

		new_pair_1 = pair[0] + middle
		new_pair_2 = middle + pair[1]
		new_occurences[new_pair_1] = new_occurences.get(new_pair_1, 0) + count
		new_occurences[new_pair_2] = new_occurences.get(new_pair_2, 0) + count

		occurrences[middle] = occurrences.get(middle, 0) + count

	pair_occurrences = new_occurences

print(max(occurrences.values()) - min(occurrences.values()))
