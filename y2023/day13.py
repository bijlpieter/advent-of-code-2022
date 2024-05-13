import numpy as np

with open("day13.txt") as fp:
    file = fp.read().strip()


def to_grid(block):
    return np.array(list(map(lambda x: list(x), block.split("\n"))))


grids = list(map(to_grid, file.split("\n\n")))


def get_size(height, idx):
    return min(idx, height - idx)


def get_reflection(grid, idx):
    size = get_size(len(grid), idx)
    return grid[idx - size : idx], grid[idx : idx + size][::-1]


def is_reflection(grid, idx):
    top, bot = get_reflection(grid, idx)
    return np.all(top == bot)


def is_almost_reflection(grid, idx):
    top, bot = get_reflection(grid, idx)
    return np.sum(top != bot) == 1


def get_reflection_indices(grid, predicate):
    return [i for i in range(1, len(grid)) if predicate(grid, i)]


rows = [i for grid in grids for i in get_reflection_indices(grid, is_reflection)]
columns = [i for grid in grids for i in get_reflection_indices(grid.T, is_reflection)]

part1 = sum(columns) + sum(row * 100 for row in rows)
print(part1)


rows = [i for grid in grids for i in get_reflection_indices(grid, is_almost_reflection)]
columns = [
    i for grid in grids for i in get_reflection_indices(grid.T, is_almost_reflection)
]

part2 = sum(columns) + sum(row * 100 for row in rows)
print(part2)
