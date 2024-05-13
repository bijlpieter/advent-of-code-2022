from math import prod

COLORS = ["red", "green", "blue"]

with open("day02.txt") as fp:
    lines = fp.read().strip().split("\n")


def parse_draw(draw):
    num, color = draw.split()
    return color, int(num)


def parse_cycle(balls):
    return dict(map(parse_draw, balls.split(", ")))


def parse_game(line):
    game, balls = line.split(": ")
    game_id = int(game.split(" ")[1])
    cycles = [parse_cycle(cycle) for cycle in balls.split("; ")]
    return game_id, cycles


games = [parse_game(line) for line in lines]


def max_balls(cycles):
    return {color: max(cycle.get(color, 0) for cycle in cycles) for color in COLORS}


def all_less(left, right):
    return all(left[color] <= right[color] for color in COLORS)


max_games = [(game_id, max_balls(cycles)) for game_id, cycles in games]


filtered_games = [
    game_id
    for game_id, maxes in max_games
    if all_less(maxes, {"red": 12, "green": 13, "blue": 14})
]

print(games[0])
print(max_games[0])
print(sum(filtered_games))
print(sum(prod(maxg.values()) for _, maxg in max_games))
