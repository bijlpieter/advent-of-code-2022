parts = {"@", "#", "/", "%", "=", "+", "$", "*", "-", "&"}


def get_input():
    with open("day03.txt") as fp:
        file = fp.read()
        lines = file.strip().split("\n")
        return list(map(list, lines))


def transform_input(grid):
    unique_id = 0
    for row in grid:
        number = ""
        for i, character in enumerate(row):
            if character.isdigit():
                number += character

            if number and (i == len(row) - 1 or not character.isdigit()):
                val = int(number)
                length = len(number)
                start = i - length + int(character.isdigit())
                row[start : start + length] = [(val, unique_id)] * length
                unique_id += 1
                number = ""


def extract_unique_numbers(grid):
    slang = []
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item in parts:
                for subrow in grid[i - 1 : i + 2]:
                    slang += subrow[j - 1 : j + 2]
    return {item for item in slang if isinstance(item, tuple)}


def gear_ratios(grid):
    counter = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == "*":
                gear_slang = []
                for subrow in grid[i - 1 : i + 2]:
                    gear_slang += subrow[j - 1 : j + 2]
                gears = {item for item in gear_slang if isinstance(item, tuple)}

                if len(gears) == 2:
                    it = iter(gears)
                    counter += next(it)[0] * next(it)[0]
    return counter


grid = get_input()
transform_input(grid)
uniques = extract_unique_numbers(grid)
part1 = sum(item[0] for item in uniques)
print(f"Part 1: {part1}")

part2 = gear_ratios(grid)
print(f"Part 2: {part2}")
