import numpy as np

with open("day04.txt") as fp:
    assignments = [i.strip().split(',') for i in fp.readlines()]

sections = np.zeros((2, len(assignments), 100), dtype=bool)

for i, asg in enumerate(assignments):
    for j in [0, 1]:
        s, e = map(int, asg[j].split('-'))
        sections[j, i, s:e+1] = True

overlap = ((sections[0] & sections[1]) == sections[0]).all(axis=1) | ((sections[0] & sections[1]) == sections[1]).all(axis=1)

print(f"Part 1: {overlap.sum()}")

overlap = sections.all(axis=0).any(axis=1)

print(f"Part 2: {overlap.sum()}")
