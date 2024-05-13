import re

with open("day01.txt") as fp:
    lines = fp.read().strip().split("\n")

digits = [[c for c in line if c.isdigit()] for line in lines]

values = [int(d[0] + d[-1]) for d in digits]

print(f"Part 1: {sum(values)}")

spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

tofind = list(spelled.keys()) + list(spelled.values())
reverse = [p[::-1] for p in tofind]

first = [re.search("|".join(tofind), line).group(0) for line in lines]  # type: ignore
last = [re.search("|".join(reverse), line[::-1]).group(0)[::-1] for line in lines]  # type: ignore
out = [int(spelled.get(a, a) + spelled.get(b, b)) for a, b in zip(first, last)]
print(f"Part 2: {sum(out)}")
