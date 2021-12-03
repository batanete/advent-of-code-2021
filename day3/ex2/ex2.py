PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.replace('\n', '') for line in f.readlines() if len(line) > 1]

def get_frequencies(lines):
	frequencies = len(lines[0]) * [0]

	for line in lines:
		for i, digit in enumerate(line):
			frequencies[i] += int(digit)
	return frequencies



electable = lines[:]
ind = 0
while len(electable) != 1:
	# if frequence > 50% of line numbers, most common is 1, else it's 0
	list_most_common = ['1' if i >= len(electable) / 2 else '0' for i in get_frequencies(electable)]
	electable = [n for n in electable if n[ind] == list_most_common[ind]]
	ind += 1

ogr = int(electable[0], 2)

electable = lines[:]
ind = 0
while len(electable) != 1:
	# if frequence > 50% of line numbers, most common is 1, else it's 0
	list_less_common = ['0' if i >= len(electable) / 2 else '1' for i in get_frequencies(electable)]
	electable = [n for n in electable if n[ind] == list_less_common[ind]]
	ind += 1

csr = int(electable[0], 2)

print(ogr * csr)