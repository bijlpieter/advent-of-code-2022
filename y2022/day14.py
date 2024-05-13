from itertools import pairwise, product

def ordered(*args):
    return sorted(args)

class Cave:
    def __init__(self, fname):
        self.cave = set()

        with open(fname) as fp:
            rocks = fp.read().strip().split("\n")

        for rock in rocks:
            self.add_rocks(rock)

    def bounds(self):
        left  = min(self.cave, key=lambda x: x[0])[0]
        right = max(self.cave, key=lambda x: x[0])[0]
        lower = max(self.cave, key=lambda x: x[1])[1]

        return left, right, lower

    def add_rocks(self, rocks):
        lines = [tuple(map(int, point.split(","))) for point in rocks.split(" -> ")]

        for start, end in pairwise(lines):
            self.draw_rock_line(start, end)

    def draw_rock_line(self, start, end):
        sx, sy = start
        ex, ey = end

        sx, ex = ordered(sx, ex)
        sy, ey = ordered(sy, ey)

        for coord in product(range(sx, ex+1), range(sy, ey+1)):
            self.cave.add(coord)

    def __str__(self):
        left, right, lower = self.bounds()
        return "\n".join(
            "".join(
                ".#"[(i, j) in self.cave] for i in range(left-1, right+2)
            )
            for j in range(lower+1)
        )

    def simulate_drop(self, until, start=(500, 0), floor=False):
        i, j = start

        for j in range(j, until):
            if (i, j+1) not in self.cave:
                continue
            
            if (i-1, j+1) not in self.cave:
                i -= 1
            elif (i+1, j+1) not in self.cave:
                i += 1
            else:
                self.cave.add((i, j))
                return True

        self.cave.add((i, j))
        return floor
    
    def collapse(self, start=(500, 0), floor=False):
        left, right, lower = self.bounds()
        count = 0
        while self.simulate_drop(lower+2, start=start, floor=floor) and start not in self.cave:
            count += 1
        return count + floor

cave = Cave("day14.txt")
print(f"Part 1: {cave.collapse(floor=False)}")

cave = Cave("day14.txt")
print(f"Part 2: {cave.collapse(floor=True)}")
