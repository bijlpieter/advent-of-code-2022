import numpy as np

class Heightmap:
    def __init__(self, fname):
        with open(fname) as fp:
            heights = np.array([list(map(lambda x: ord(x) - ord('a') + 1, x.strip())) for x in fp.readlines()])

        self.heights = np.pad(heights, 1)

        start = np.where(self.heights == -13)
        end = np.where(self.heights == -27)

        self.start = (end[0][0], end[1][0])
        self.end = (start[0][0], start[1][0])

        self.heights[start] = 1
        self.heights[end] = 26

    def neighbors(self, v):
        x, y = v
        for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if not self.visited[n] and self.heights[v] <= self.heights[n] + 1:
                yield n

    def next_loc(self):
        return np.unravel_index(np.ma.array(self.dist, mask=self.visited).argmin(), shape=self.dist.shape)

    def dijkstra(self):
        h, w = self.heights.shape
        self.dist = np.full((h, w), np.inf)
        self.visited = np.pad(np.zeros((h-2, w-2), dtype=bool), 1, constant_values=True)
        self.dist[self.start] = 0

        while not self.visited.all():
            v = self.next_loc()
            self.visited[v] = True
            d = self.dist[v]
            if np.isinf(d):
                return

            for w in self.neighbors(v):
                self.dist[w] = min(self.dist[w], d + 1)

    def start_to_end_dist(self):
        return int(self.dist[self.end])

    def best_trail_dist(self):
        return int(self.dist[self.heights == 1].min())

heightmap = Heightmap("day12.txt")
heightmap.dijkstra()
print(f"Part 1: {heightmap.start_to_end_dist()}")
print(f"Part 2: {heightmap.best_trail_dist()}")
