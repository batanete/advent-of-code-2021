PATH = 'ex2.txt'

N_DAYS = 256
TIMER_AFTER_SPAWN = 6
TIMER_AFTER_BIRTH = 8
N_POSSIBLE_TIMERS = max(TIMER_AFTER_SPAWN, TIMER_AFTER_BIRTH) + 1

def process(seafishes):

	for day in range(N_DAYS):
		births = seafishes[0]

		for timer in range(0, N_POSSIBLE_TIMERS - 1):
			seafishes[timer] = seafishes[(timer + 1) % N_POSSIBLE_TIMERS]

		seafishes[TIMER_AFTER_SPAWN] += births
		seafishes[TIMER_AFTER_BIRTH] = births
		
	return sum(seafishes)


with open(PATH) as f:
	lines = [line.strip() for line in f.readlines()]

timers = lines[0].split(',')

seafishes = [0] * N_POSSIBLE_TIMERS
for timer_str in timers:
	timer = int(timer_str)

	seafishes[timer] += 1

final_count = process(seafishes)
print(final_count)