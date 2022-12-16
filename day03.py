from functools import reduce
import operator

def split(x):
	n = len(x) // 2
	return set(x[:n]), set(x[n:])

def get_duplicate(x):
	unique = reduce(operator.__and__, x)
	return next(iter(unique))

def priority(c):
	return ord(c) - (96 if c.islower() else 38)

def priorities(x):
	return sum(priority(c) for c in x)

with open("day03.txt") as fp:
	rucksacks = fp.read().strip().split("\n")

common = [
	get_duplicate(split(x))
	for x in rucksacks
]
print(f"Part 1: {priorities(common)}")

common = [
	get_duplicate(map(set, i))
	for i in zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3])
]
print(f"Part 2: {priorities(common)}")
