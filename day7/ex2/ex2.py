PATH = 'ex2.txt'

with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

def distance(p1, p2):
	dist = abs(p1 - p2)
	return sum(range(1, dist + 1))

crabs = [int(i) for i in lines[0].split(',')]

horizontal_size = max(crabs) + 1

crab_counts = [0] * horizontal_size

for crab in crabs:
	crab_counts[crab] += 1

best_fuel = None
for position in range(horizontal_size + 1):
	fuel_needed = sum([distance(position, ind) * crab_count for ind, crab_count in enumerate(crab_counts)])

	if best_fuel is None or fuel_needed < best_fuel:
		best_fuel = fuel_needed

print(best_fuel)