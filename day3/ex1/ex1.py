PATH = 'ex1.txt'

with open(PATH) as f:
	lines = [line.replace('\n', '') for line in f.readlines()]

n_lines = len(lines)

size_n = len(lines[0])
frequences = size_n * [0]

for line in lines:
	for i, digit in enumerate(line):
		frequences[i] += int(digit)

# if frequence > 50% of line numbers, most common is 1, else it's 0
list_gamma_rate = ['1' if i >= n_lines / 2 else '0' for i in frequences]
list_epsilon_rate = ['0' if i >= n_lines / 2 else '1' for i in frequences]

print(list_gamma_rate)
print(list_epsilon_rate)

gamma_rate = int(''.join(list_gamma_rate), 2)
epsilon_rate = int(''.join(list_epsilon_rate), 2)

print(gamma_rate * epsilon_rate)