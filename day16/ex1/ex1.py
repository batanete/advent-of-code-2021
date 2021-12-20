PATH = 'ex1.txt'

def process_packet(bin_str, start):
	ind = start
	versions = 0

	version = int(bin_str[ind : ind + 3], 2)
	type_id = int(bin_str[ind + 3 : ind + 6], 2)

	ind += 6
	versions += version

	# literal, simply advance till the end
	if type_id == 4:
		while True:
			ind += 5
			if bin_str[ind-5] == '0':
				break

	# operator, need to traverse all subpackets
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

		ind, new_versions = res
		versions += new_versions

	return ind, versions


def process_packets_in_length(bin_str, start, length):
	ind = start
	versions = 0

	while ind < start + length:
		ind, new_versions = process_packet(bin_str, ind)
		versions += new_versions

	return ind, versions


def process_n_packets(bin_str, start, n_packets):
	versions = 0
	ind = start
	for _ in range(n_packets):
		ind, new_versions = process_packet(bin_str, ind)
		versions += new_versions

	return ind, versions

def solve_bin(bin_str):
	#print("bin:{}".format(bin_str))
	return process_packet(bin_str, 0)[1]


def solve_hex(hex_str):
	#print("hex:{}".format(hex_str))

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
