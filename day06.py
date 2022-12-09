import pandas as pd

with open("day06.txt") as fp:
    signal = [ord(i) for i in fp.read().strip()]

def unique_substr_of_len(signal, n):
    return pd.Series(signal).rolling(n).apply(lambda x: len(set(x))).eq(n).argmax() + 1

print(f"Part 1: {unique_substr_of_len(signal, n=4)}")

print(f"Part 2: {unique_substr_of_len(signal, n=14)}")
