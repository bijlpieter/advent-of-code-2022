import numpy as np
import pandas as pd

with open("day1.txt") as fp:
	ragged = [i.strip().split("\n") for i in fp.read().split("\n\n")]

calories = pd.DataFrame(ragged).fillna(0).astype(int).sum(axis=1)

print(f"Part 1: {calories.max()}")
print(f"Part 2: {calories.nlargest(3).sum()}")
