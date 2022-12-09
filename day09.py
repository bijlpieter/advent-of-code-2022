import numpy as np

dirs = {
	'D': np.array([-1, 0]),
	'U': np.array([1, 0]),
	'L': np.array([0, -1]),
	'R': np.array([0, 1]),
}

tail_offset = np.array([
	[[-1, -1], [-1, -1], [-1,  0], [-1,  1], [-1,  1]],
	[[-1, -1], [ 0,  0], [ 0,  0], [ 0,  0], [-1,  1]],
	[[ 0, -1], [ 0,  0], [ 0,  0], [ 0,  0], [ 0,  1]],
	[[ 1, -1], [ 0,  0], [ 0,  0], [ 0,  0], [ 1,  1]],
	[[ 1, -1], [ 1, -1], [ 1,  0], [ 1,  1], [ 1,  1]]
])

class Rope:
	def __init__(self, fname, n=2):
		self.n = n
		self.knots = [np.zeros(2, dtype=int) for _ in range(n)]
		self.visited = {(0, 0)}

		with open(fname) as fp:
			instructions = [i.strip().split() for i in fp.readlines()]

		for direction, count in instructions:
			self.move(direction, int(count))

	def move(self, direction, count):
		offset = dirs[direction]

		for _ in range(count):
			self.do_move(offset)

	def do_move(self, offset):
		self.knots[0] += offset

		for i in range(1, self.n):
			self.knots[i] += tail_offset[tuple(self.knots[i-1] - self.knots[i] + 2)]

		self.visited.add(tuple(self.knots[-1]))

	def num_visited(self):
		return len(self.visited)

rope = Rope("day09.txt", n=2)
print(f"Part 1: {rope.num_visited()}")

rope = Rope("day09.txt", n=10)
print(f"Part 1: {rope.num_visited()}")
