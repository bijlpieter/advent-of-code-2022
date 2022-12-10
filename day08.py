import numpy as np
import pandas as pd

with open("day08.txt") as fp:
    df = pd.DataFrame([list(map(int, x.strip())) for x in fp.readlines()])

north = df.cummax(axis=0).diff(axis=0).ne(0)
south = df.iloc[::-1, :].cummax(axis=0).diff(axis=0).ne(0)

west = df.cummax(axis=1).diff(axis=1).ne(0)
east = df.iloc[:, ::-1].cummax(axis=1).diff(axis=1).ne(0)

print(f"Part 1: {(north | south | west | east).values.sum()}")

grid = df.values
h, w = grid.shape  
scenic_scores = np.ones_like(grid)

def calculate_distance(x, y, dx, dy):
    for dist in range(1, max(h, w)+1):
        new_x, new_y = x + dist * dx, y + dist * dy
        if not (0 <= new_x < h and 0 <= new_y < w):
            return dist-1

        if (grid[new_x, new_y] >= value):
            return dist
    return 0

for (x, y), value in np.ndenumerate(grid):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        scenic_scores[x, y] *= calculate_distance(x, y, dx, dy)

print(f"Part 2: {scenic_scores.max()}")
