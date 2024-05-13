from itertools import cycle
from math import lcm

with open("day08.txt") as fp:
    file = fp.read().strip()

instructions, nodes = file.split("\n\n")
directions = enumerate(cycle(instructions), start=1)


def parse_line(line):
    node, destinations = line.split(" = ")
    left, right = destinations.split(", ")
    return node, {"L": left[1:], "R": right[:-1]}


network = dict(map(parse_line, nodes.split("\n")))
print(network)


def solve(curr, end):
    directions = enumerate(cycle(instructions), start=1)
    while not end(curr):
        count, next_dir = next(directions)
        curr = network[curr][next_dir]

    return count


print(solve("AAA", lambda x: x == "ZZZ"))

counts = [
    solve(loc, lambda x: x[-1] == "Z") for loc in network.keys() if loc[-1] == "A"
]
print(lcm(*counts))

# count = 0
# counts = [0] * len(currs)
# while not all(loc[-1] == "Z" for loc in currs):
#     # print(currs)
#     count, next_dir = next(directions)
#     currs = [network[loc][next_dir] for loc in currs]
#     counts = [
#         print(c, n) or 0 if n[-1] == "Z" else c + 1 for c, n in zip(counts, currs)
#     ]
#     # print(counts)
