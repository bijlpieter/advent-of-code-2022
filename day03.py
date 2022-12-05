import numpy as np
import pandas as pd

with open("day03.txt") as fp:
	rucksacks = [i.strip() for i in fp.readlines()]

common = [
	next(iter(set(x[:len(x)//2]).intersection(set(x[len(x)//2:]))))
	for x in rucksacks
]
priorities = [ord(c) - (96 if c.islower() else 38) for c in common]

print(f"Part 1: {sum(priorities)}")

common = [
	next(iter(set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2]))))
	for i in range(0, len(rucksacks), 3)
]
priorities = [ord(c) - (96 if c.islower() else 38) for c in common]

print(f"Part 2: {sum(priorities)}")
