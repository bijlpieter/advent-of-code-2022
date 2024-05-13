import numpy as np
from functools import cmp_to_key

def isint(val): return isinstance(val, int)
def islist(val): return isinstance(val, list)
def aslist(val): return val if islist(val) else [val]

def compare(left, right):
	if isint(left) and isint(right):
		return np.sign(left - right)

	if islist(left) != islist(right):
		return compare(aslist(left), aslist(right))
	
	if not left or not right:
		return bool(left) - bool(right)

	lhead, *ltail = left
	rhead, *rtail = right

	out = compare(lhead, rhead)
	return out if out else compare(ltail, rtail)

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
