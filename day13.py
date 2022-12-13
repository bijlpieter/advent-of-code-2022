import numpy as np

def as_list(val):
	return val if isinstance(val, list) else [val]

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int):
		return np.sign(left - right)

	if isinstance(left, list) and isinstance(right, list):
		if not left or not right:
			return bool(left) - bool(right)

		out = compare(left[0], right[0])

		return out if out else compare(left[1:], right[1:])

	return compare(as_list(left), as_list(right))

class Packet:
	def __init__(self, pstr):
		self.x = eval(pstr)

	def __lt__(self, other):
		return compare(self.x, other.x) == -1

	def __eq__(self, other):
		return compare(self.x, other.x) == 0

	def __gt__(self, other):
		return compare(self.x, other.x) == 1

	def __str__(self):
		return str(self.x)

with open("day13.txt") as fp:
	pairs = fp.read().strip().split("\n\n")

lists = [
	(Packet(left), Packet(right))
	for pair in pairs
	for left, right in [pair.split("\n")]
]

order = np.array([compare(left.x, right.x) for left, right in lists])

print(f"Part 1: {np.arange(1, len(order)+1)[order < 0].sum()}")

div_one, div_two = Packet("[[2]]"), Packet("[[6]]")

all_lists = [l for pair in lists for l in pair] + [div_one, div_two]
ordered = sorted(all_lists)

one, two = ordered.index(div_one) + 1, ordered.index(div_two) + 1

print(f"Part 2: {one * two}")
