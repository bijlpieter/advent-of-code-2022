from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from functools import cache
from itertools import product
from typing import Iterator

with open("day24.txt") as fp:
    file = fp.read().strip()


directions = {"v": (1, 0), "<": (0, -1), ">": (0, 1), "^": (-1, 0)}


@dataclass
class Valley:
    grid: list[list[str]]
    size: tuple[int, int]

    def coords(self) -> Iterator[tuple[int, int]]:
        h, w = self.size
        return product(range(1, h), range(1, w))

    def move_blizzard(self, loc: tuple[int, int], char: str) -> tuple[int, int]:
        h, w = self.size
        i, j = loc
        di, dj = directions.get(char, (0, 0))
        ni, nj = i + di, j + dj

        if ni == 0:
            ni = h - 1
        if ni == h:
            ni = 1

        if nj == 0:
            nj = w - 1
        if nj == w:
            nj = 1

        return ni, nj

    def player_moves(self, loc: tuple[int, int]) -> Iterator[tuple[int, int]]:
        i, j = loc
        h, w = self.size
        for di, dj in [(1, 0), (0, -1), (0, 1), (-1, 0), (0, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni <= h and 0 <= nj <= w and not self.grid[ni][nj]:
                yield ni, nj

    def empty_copy(self) -> Valley:
        valley = deepcopy(self)
        for i, j in self.coords():
            valley.grid[i][j] = ""
        return valley

    def simulate(self) -> Valley:
        valley = self.empty_copy()
        for i, j in self.coords():
            for char in self.grid[i][j]:
                ni, nj = self.move_blizzard((i, j), char)
                valley.grid[ni][nj] += char
        return valley

    def start_end(self) -> tuple[tuple[int, int], tuple[int, int]]:
        h, w = self.size
        return (0, 1), (h, w - 1)

    @staticmethod
    def from_line(line: str) -> list[str]:
        return ["" if char == "." else char for char in line]

    @staticmethod
    def from_text(text: str) -> Valley:
        grid: list[list[str]] = list(map(Valley.from_line, text.split("\n")))  # type: ignore
        size = (len(grid) - 1, len(grid[0]) - 1)
        return Valley(grid, size)

    def __str__(self) -> str:
        return "\n".join(
            "".join([".", char, *"2345"][len(char)] for char in row)
            for row in self.grid
        )


start_valley = Valley.from_text(file)


@cache
def get_valley(k: int) -> Valley:
    return start_valley if k == 0 else get_valley(k - 1).simulate()


def bfs(start: tuple[int, int], end: tuple[int, int], cyc=0) -> int:
    visited: set[tuple[int, int, int]] = {(*start, cyc)}
    queue: list[tuple[int, int, int]] = [(*start, cyc)]

    while queue:
        i, j, cycle = queue.pop(0)
        next_cycle = cycle + 1
        # print(i, j, next_cycle)
        valley = get_valley(next_cycle)

        for pos in valley.player_moves((i, j)):
            if pos == end:
                return next_cycle

            neighbor = (*pos, next_cycle)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return -1


start, end = start_valley.start_end()

one = bfs(start, end, 0)
print(one)
two = bfs(end, start, one)
print(two)
three = bfs(start, end, two)
print(three)
