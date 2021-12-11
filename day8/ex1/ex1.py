PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

num_by_segments = {
	2: 1,
	4: 4,
	3: 7,
	7: 8,
}

result = 0
for line in lines:
	toks = [tok.strip() for tok in line.split('|')]

	output_values = toks[1].split(' ')

	output_value_sizes = [len(value) for value in output_values]
	result += len(
		list(
			filter(lambda n: n in num_by_segments.keys(), output_value_sizes)
		)
	)

print(result)