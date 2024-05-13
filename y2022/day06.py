import pandas as pd

with open("day06.txt") as fp:
    signal = list(map(ord, fp.read().strip()))

def all_different(x):
    return x.nunique() == len(x)

def unique_substr_of_len(signal, n):
    return signal.rolling(n).apply(all_different).idxmax()

series = pd.Series(
    signal,
    index=pd.RangeIndex(1, len(signal)+1),
)

print(f"Part 1: {unique_substr_of_len(series, n=4)}")
print(f"Part 2: {unique_substr_of_len(series, n=14)}")
