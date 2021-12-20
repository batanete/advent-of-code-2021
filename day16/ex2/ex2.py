from functools import reduce

PATH = 'ex2.txt'

def parse_literal(bin_str, start):
	bits = []
	ind = start
	while bin_str[ind] == '1':
		bits.append(bin_str[ind + 1 : ind + 5])
		ind += 5
	bits.append(bin_str[ind + 1 : ind + 5])
	ind += 5

	value = int(''.join(bits), 2)
	return ind, value

def apply_operator(values, type_id):
	if type_id == 0:
		return sum(values)
	elif type_id == 1:
		return reduce(lambda x,y: x * y, values)
	elif type_id == 2:
		return min(values)
	elif type_id == 3:
		return max(values)
	elif type_id == 5:
		return 1 if values[0] > values[1] else 0
	elif type_id == 6:
		return 1 if values[0] < values[1] else 0
	elif type_id == 7:
		return 1 if values[0] == values[1] else 0

def process_packet(bin_str, start):
	ind = start

	# we don't need the version now
	type_id = int(bin_str[ind + 3 : ind + 6], 2)
	ind += 6

	value = None

	# literal, parse it and return value
	if type_id == 4:
		ind, value = parse_literal(bin_str, ind)

	# operator, need to traverse all subpackets and apply operation to them
	else:
		mode = bin_str[ind]
		ind += 1

		if mode == '0':
			packet_length = int(bin_str[ind : ind + 15], 2)
			ind += 15
			res = process_packets_in_length(bin_str, ind, packet_length)
		else:
			n_packets = int(bin_str[ind : ind + 11], 2)
			ind += 11
			res = process_n_packets(bin_str, ind, n_packets)

		ind, values = res

		value = apply_operator(values, type_id)

	return ind, value


def process_packets_in_length(bin_str, start, length):
	ind = start
	values = []

	while ind < start + length:
		ind, value = process_packet(bin_str, ind)
		values.append(value)

	return ind, values


def process_n_packets(bin_str, start, n_packets):
	versions = 0
	ind = start
	values = []
	for _ in range(n_packets):
		ind, value = process_packet(bin_str, ind)
		values.append(value)

	return ind, values

def solve_bin(bin_str):
	return process_packet(bin_str, 0)[1]


def solve_hex(hex_str):
	bins = []
	for chunk in hex_str:
		bin_chunk = bin(int(chunk, 16))[2:]
		# add trailing zeroes
		while len(bin_chunk) != 4:
			bin_chunk = '0' + bin_chunk
		bins.append(bin_chunk)

	return solve_bin(''.join(bins))

if __name__ == '__main__':
	with open(PATH) as f:
		line = f.readline().strip()

	result = solve_hex(line)
	print(result)


#assert solve_bin('110100101111111000101000') == 2021
#assert solve_hex('C200B40A82') == 3
#assert solve_hex('04005AC33890') == 54
#assert solve_hex('880086C3E88112') == 7
#assert solve_hex('CE00C43D881120') == 9
#assert solve_hex('D8005AC2A8F0') == 1
#assert solve_hex('F600BC2D8F') == 0
#assert solve_hex('9C005AC2F8F0') == 0
#assert solve_hex('9C0141080250320F1802104A08') == 1

# C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
# 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
# 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
# CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
# D8005AC2A8F0 produces 1, because 5 is less than 15.
# F600BC2D8F produces 0, because 5 is not greater than 15.
# 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
# 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2
