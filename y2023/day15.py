with open("day15.txt") as fp:
    grid = fp.read().strip().split("\n")
    h, w = len(grid), len(grid[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def beam(row: int, col: int, dir: int, traversed: set[tuple[int, int, int]]):
    while True:
        dir %= 4
        dr, dc = directions[dir]
        row, col = row + dr, col + dc

        if (row, col, dir) in traversed:
            return

        if not (0 <= row < h and 0 <= col < w):
            return

        symbol = grid[row][col]
        traversed.add((row, col, dir))

        if symbol == "\\":
            dir = dir - bool(dr) + bool(dc)
        elif symbol == "/":
            dir = dir + bool(dr) - bool(dc)
        elif (symbol == "-" and dr) or (symbol == "|" and dc):
            beam(row, col, dir + 1, traversed)
            beam(row, col, dir - 1, traversed)
            return


def execute(row: int, col: int, dir: int) -> int:
    traversed = set()
    beam(row, col, dir, traversed)
    return len(set((r, c) for r, c, _ in traversed))


print(execute(0, -1, 0))
print(
    max(
        [
            *[execute(row, -1, 0) for row in range(h)],
            *[execute(-1, col, 1) for col in range(w)],
            *[execute(h, col, 2) for col in range(w)],
            *[execute(row, w, 3) for row in range(h)],
        ]
    )
)
