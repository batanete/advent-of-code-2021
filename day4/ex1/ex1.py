from sys import exit

PATH = 'ex1.txt'

class Board:

	def __init__(self, lines):
		self.rows = []
		for line in lines:
			self.rows.append([[int(num), False] for num in line.split()])

	# returns score if board won, -1 otherwise
	# assuming boards have no repeated numbers, like in real life bingo
	def process_number(self, num):
		for i, row in enumerate(self.rows):
			for j, el in enumerate(row):
				if el[0] == num:
					el[1] = True
					if self._row_has_won(i) or self._col_has_won(j):
						return self._score() * num

		return -1

	def _row_has_won(self, index):
		return all([el[1] for el in self.rows[index]])

	def _col_has_won(self, index):
		# assuming columns have the same length as rows, like in real life bingo
		col = [row[index] for row in self.rows]
		return all([el[1] for el in col])

	def _score(self):
		score = 0
		for row in self.rows:
			score += sum([el[0] for el in row if not el[1]])

		return score 


def read_game_numbers(f):
	return [int(n) for n in f.readline().split(',')]

def read_boards(f):
	# skip empty lines
	lines = [line.strip() for line in f.readlines() if len(line) > 1]

	boards = []
	ind = 0
	while ind < len(lines):
		boards.append(Board(lines[ind:ind+5]))
		ind += 5

	return boards

with open(PATH) as f:
	nums = read_game_numbers(f)
	boards = read_boards(f)

for num in nums:
	for board in boards:
		score = board.process_number(num)
		if score >= 0:
			print(score)
			exit(0)


