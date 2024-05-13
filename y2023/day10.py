import numpy as np

with open("day10.txt") as fp:
    file = fp.read().strip()

grid = np.array(list(map(lambda x: list(x), file.split("\n"))))


North, East, South, West = (-1, 0), (0, 1), (1, 0), (0, -1)
NESW = {North, East, South, West}

directions = {
    "|": [North, South],
    "-": [East, West],
    "L": [North, East],
    "J": [North, West],
    "7": [South, West],
    "F": [South, East],
    ".": [],
    "S": [North, West],
}


def find_start(grid: list[str]):
    for i, line in enumerate(grid):
        if "S" in line:
            return i, line.index("S")
    return (-1, -1)


def move(position, direction):
    i, j = position
    di, dj = direction
    return i + di, j + dj


def get_directions(position):
    return directions[grid[position]]


def get_next_pos(curr, visited):
    one, two = get_directions(curr)
    left, right = move(curr, one), move(curr, two)
    return left if visited[right] else right


H, W = grid.shape
visited = np.zeros_like(grid, dtype=bool)
start = tuple(np.argwhere(grid == "S")[0])
visited[start] = True


left_dir, right_dir = get_directions(start)
left, right = move(start, left_dir), move(start, right_dir)

count = 1
while left != right:
    count += 1

    new_left = get_next_pos(left, visited)
    new_right = get_next_pos(right, visited)

    visited[left] = True
    visited[right] = True

    left, right = new_left, new_right

visited[left] = True

loop = np.where(visited, grid, ".")
side = np.zeros_like(grid, dtype=int)

print(count)
print("\n".join("".join(row) for row in loop))
print(H, W)

dashes = np.cumsum(loop == "-", axis=0)
wests = np.cumsum(np.isin(loop, list("7JS")), axis=0)
easts = np.cumsum(np.isin(loop, list("FL")), axis=0)
total = dashes + np.minimum(wests, easts)
inside = (total % 2) & (loop == ".")

print("\n".join("".join(row) for row in np.where(inside, "#", ".")))
print(inside.astype(bool).sum())

dashes = np.cumsum(loop == "|", axis=1)
wests = np.cumsum(np.isin(loop, list("LJS")), axis=1)
easts = np.cumsum(np.isin(loop, list("F7")), axis=1)
total = dashes + np.minimum(wests, easts)
inside = (total % 2) & (loop == ".")

print("\n".join("".join(row) for row in np.where(inside, "#", ".")))
print(inside.astype(bool).sum())
