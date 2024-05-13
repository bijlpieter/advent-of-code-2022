from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


def middle_subset(sub: range, super: range) -> bool:
    return super.start < sub.start and sub.stop < super.stop


def fully_contained(sub: range, super: range) -> bool:
    return super.start <= sub.start and sub.stop <= super.stop


def find_intersection(current: range, target: range) -> range:
    return range(max(current.start, target.start), min(current.stop, target.stop))


def find_difference(current: range, hits: range) -> list[range]:
    if middle_subset(hits, current):
        return [range(current.start, hits.start), range(hits.stop, current.stop)]

    if current.start == hits.start:
        return [range(hits.stop, current.stop)]
    else:
        return [range(current.start, hits.start)]


def partition(current: range, target: range) -> tuple[range | None, list[range]]:
    """
    Returns:
    The part of `current` that is not inside `target`,
    The part of `current` that is inside `target`

    1-5, 13-18
    3-5, 1-3
    """

    no_intersection = current.start > target.stop or current.stop < target.start
    if no_intersection:
        return None, [current]

    full_intersection = fully_contained(current, target)
    if full_intersection:
        return current, []

    hits = find_intersection(current, target)
    remainder = find_difference(current, hits)

    return hits, remainder


@dataclass
class CategorySubmap:
    dst: int
    src: int
    size: int

    def __contains__(self, val: int) -> bool:
        return self.src <= val < self.src + self.size

    def convert(self, val: int) -> int:
        return self.dst + val - self.src

    def convert_range(self, val: range) -> tuple[range | None, list[range]]:
        """
        Returns:
        The part of `val` that was mapped to a new range,
        The parts of `val` that still remain to be mapped.
        """
        hits, remainder = partition(val, range(self.src, self.src + self.size))
        if hits is None:
            return hits, remainder

        converted = self.convert(hits.start)
        mapped = range(converted, converted + len(hits))
        return mapped, remainder

    @staticmethod
    def from_line(line: str) -> CategorySubmap:
        return CategorySubmap(*map(int, line.split()))


@dataclass
class CategoryMapping:
    name: str
    maps: list[CategorySubmap]

    def convert(self, val: int) -> int:
        for submap in self.maps:
            if val in submap:
                return submap.convert(val)
        return val

    def convert_range(self, val: range, map_index: int = 0) -> Iterator[range]:
        done, remainder = self.maps[map_index].convert_range(val)
        if done:
            yield done
        if remainder:
            yield from self.multi_convert_ranges(remainder, map_index=map_index + 1)

    def multi_convert(self, inputs: list[int]) -> list[int]:
        return [self.convert(val) for val in inputs]

    def multi_convert_ranges(
        self, ranges: list[range], map_index: int = 0
    ) -> list[range]:
        if map_index >= len(self.maps):
            return ranges
        return [
            out
            for val in ranges
            for out in self.convert_range(val, map_index=map_index)
        ]

    @staticmethod
    def from_block(lines: str) -> CategoryMapping:
        name, *maps = lines.strip().split("\n")
        return CategoryMapping(
            name=name, maps=list(map(CategorySubmap.from_line, maps))
        )


@dataclass
class Farm:
    mappings: list[CategoryMapping]

    def haal_seeds_door_alle_kanker_mappings(self, seeds: list[int]) -> list[int]:
        for mapping in self.mappings:
            seeds = mapping.multi_convert(seeds)
        return seeds

    def haal_ranges_door_alle_kanker_mappings(self, ranges: list[range]) -> list[range]:
        for mapping in self.mappings:
            ranges = mapping.multi_convert_ranges(ranges)
        return ranges

    @staticmethod
    def from_block_list(blocks: list[str]) -> Farm:
        return Farm(mappings=list(map(CategoryMapping.from_block, blocks)))


with open("day05.txt") as fp:
    file = fp.read()

seeds_in, *blocks = file.split("\n\n")
farm = Farm.from_block_list(blocks)
seeds = list(map(int, seeds_in.split()[1:]))


def get_ranges(seeds) -> list[range]:
    starts, lengths = seeds[::2], seeds[1::2]
    return [range(start, start + length) for start, length in zip(starts, lengths)]


def part1():
    out = farm.haal_seeds_door_alle_kanker_mappings(seeds)
    print(min(out))


def part2():
    ranges = get_ranges(seeds)
    out = farm.haal_ranges_door_alle_kanker_mappings(ranges)
    print(min(r.start for r in out))


part1()
part2()
