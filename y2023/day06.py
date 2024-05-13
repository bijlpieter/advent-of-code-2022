import re
from math import prod

with open("day06.txt") as fp:
    file = fp.read().strip()


def parse_line(line):
    parts = re.split(r"\s+", line)[1:]
    return list(map(int, parts))


def parse_line_2(line):
    parts = re.split(r"\s+", line)[1:]
    return int("".join(parts))


times, records = map(parse_line, file.split("\n"))


def solve(time, record):
    return sum(i * (time - i) > record for i in range(time + 1))


print(prod(solve(t, r) for t, r in zip(times, records)))
# distances = [[i * (t - i) for i in range(t + 1)] for t in times]
# wins = [sum(d > r for d in dists) for dists, r in zip(distances, records)]
# print(prod(wins))

time, record = map(parse_line_2, file.split("\n"))
print(solve(time, record))
