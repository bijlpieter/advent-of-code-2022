import numpy as np
from functools import cmp_to_key

def aslist(val): return val if isinstance(val, list) else [val]
def isint(val): return isinstance(val, int)
def islist(val): return isinstance(val, list)

def compare(left, right):
	if isint(left) and isint(right):
		return np.sign(left - right)

	if islist(left) and islist(right):
		if not left or not right:
			return bool(left) - bool(right)

		out = compare(left[0], right[0])
		return out if out else compare(left[1:], right[1:])

	return compare(aslist(left), aslist(right))

with open("day13.txt") as fp:
	pairs = fp.read().strip().split("\n\n")

lists = [
	(eval(left), eval(right))
	for pair in pairs
	for left, right in [pair.split("\n")]
]

order = np.array([compare(left, right) for left, right in lists])
print(f"Part 1: {np.arange(1, len(order)+1)[order < 0].sum()}")

div_one, div_two = [[2]], [[6]]
all_lists = [l for pair in lists for l in pair] + [div_one, div_two]
ordered = sorted(all_lists, key=cmp_to_key(compare))
one, two = ordered.index(div_one) + 1, ordered.index(div_two) + 1
print(f"Part 2: {one * two}")
