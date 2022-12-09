import numpy as np

with open("day02.txt") as fp:
	strategy = [i.split() for i in fp.readlines()]

indices = np.array(strategy).view(dtype=int) - [ord('A'), ord('X')]
x, y = indices.T

scores = np.array([
	[4, 8, 3],
	[1, 5, 9],
	[7, 2, 6],
])

print(f"Part 1: {scores[x, y].sum()}")

scores = np.array([
	[3, 4, 8],
	[1, 5, 9],
	[2, 6, 7],
])

print(f"Part 2: {scores[x, y].sum()}")
