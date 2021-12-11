PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

unique_num_by_segments = {
	2: 1,
	4: 4,
	3: 7,
	7: 8,
}

def contains_all_chars_of_other(str1, str2):
	for c in str2:
		if c not in str1:
			return False
	return True

def solve(signals, output_values):
	num_to_signal = {}
	signal_to_num = {}
	# first we compute signals with unique lengths(1,4,7,8)
	for signal in signals:
		if len(signal) in unique_num_by_segments.keys():
			num = unique_num_by_segments[len(signal)]
			num_to_signal[num] = signal
			signal_to_num[signal] = num

	for unique_signal in signal_to_num.keys():
		signals.remove(unique_signal)

	# only 3 has 5 segments and contains the segments for '7'
	for signal in signals:
		if len(signal) == 5 and contains_all_chars_of_other(signal, num_to_signal[7]):
			num_to_signal[3] = signal
			signal_to_num[signal] = 3
			signals.remove(signal)
			break

	# only 9 'contains' 3 and has num of segments=6
	for signal in signals:
		if len(signal) == 6 and contains_all_chars_of_other(signal, num_to_signal[3]):
			num_to_signal[9] = signal
			signal_to_num[signal] = 9
			signals.remove(signal)
			break

	# only 6 has num of segments = 6 and doesn't contain all letters of '1'
	for signal in signals:
		if len(signal) == 6 and not contains_all_chars_of_other(signal, num_to_signal[1]):
			num_to_signal[6] = signal
			signal_to_num[signal] = 6
			signals.remove(signal)
			break


	# we only have the signals for 0, 2 and 5 left. 0 is the one of the three with 6 segments.
	for signal in signals:
		if len(signal) == 6:
			num_to_signal[0] = signal
			signal_to_num[signal] = 0
			signals.remove(signal)
			break

	# we only have the signals for 2 and 5 left. 5 is the one which only has one non matching segment with 6
	# that leaves only 2
	for signal in signals:
		non_matches = 0
		for letter in num_to_signal[6]:
			if letter not in signal:
				non_matches += 1
		if non_matches == 1:
			num_to_signal[5] = signal
			signal_to_num[signal] = 5
		else:
			num_to_signal[2] = signal
			signal_to_num[signal] = 2

	decyphered_values_str = [str(signal_to_num[value]) for value in output_values]
	result = int(''.join(decyphered_values_str))
	return result


result = 0
for line in lines:
	toks = [tok.strip() for tok in line.split('|')]

	signals = toks[0].split(' ')
	output_values = toks[1].split(' ')

	# sort values to prevent ambiguities
	signals = [''.join(sorted(signal)) for signal in signals]
	output_values = [''.join(sorted(value)) for value in output_values]

	result += solve(signals, output_values)

print(result)
