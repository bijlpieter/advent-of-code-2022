import pandas as pd

def get_interval(istr):
    left, right = istr.split("-")
    return pd.Interval(int(left), int(right), closed="both")

with open("day04.txt") as fp:
    intervals = [
        tuple(map(get_interval, duo.split(",")))
        for duo in fp.read().strip().split("\n")
    ]

print(f"Part 1: {sum(one in two or two in one for one, two in intervals)}")
print(f"Part 2: {sum(one.overlaps(two) for one, two in intervals)}")
