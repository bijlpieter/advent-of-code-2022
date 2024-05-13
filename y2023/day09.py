with open("day09.txt") as fp:
    file = fp.read().strip()

lines = [list(map(int, line.split(" "))) for line in file.split("\n")]
print(lines)


def diff(line):
    return [b - a for a, b in zip(line, line[1:])]


def all_zero(line):
    return all(i == 0 for i in line)


def extrapolate(final_vals, right=True):
    val = 0
    sign = 1 if right else -1
    for i in final_vals:
        val = i + val * sign
    return val


def solve(line, right=True):
    final_vals = []
    idx = -1 if right else 0
    while not all_zero(line):
        final_vals.append(line[idx])
        line = diff(line)
    return extrapolate(final_vals[::-1], right)


print(sum(solve(line, right=True) for line in lines))
print(sum(solve(line, right=False) for line in lines))
# print(solve([10, 13, 16, 21, 30, 45], right=False))
