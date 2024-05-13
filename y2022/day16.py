# import numpy as np
# import pandas as pd
# import itertools
# from dataclasses import dataclass, field

# @dataclass
# class Valve:
#     name: str = ""
#     flowrate: int = 0
#     neighbors: frozenset[str] = field(default_factory=frozenset)

# class Volcano:
#     def __init__(self, fname):
#         with open(fname) as fp:
#             valves = fp.readlines()

#         self.valves = {
#             tokens[1]: Valve(
#                 name=tokens[1],
#                 flowrate=int(tokens[4][5:-1]),
#                 neighbors=[
#                     neighbor[:-1] for neighbor in tokens[9:]
#                 ]
#             )
#             for line in valves
#             for tokens in [line.split(" ")]
#         }

#         self.index = [k for k, v in self.valves.items() if v.flowrate]
#         self.n = len(self.index)

#         self.dist = self.calc_distances()

#     def calc_distances(self):
#         series = [self.dijkstra(valve_id) for valve_id in self.index]
#         return pd.concat(series, keys=self.index, axis=1).astype(int)

#     def dijkstra(self, valve_id):
#         dist = pd.Series(np.full(self.n, np.inf), index=self.index)
#         visited = pd.Series(np.zeros(self.n), index=self.index, dtype=bool)

#         dist[valve_id] = 0

#         while not visited.all():
#             v = dist[~visited].idxmin()
#             visited[v] = True
#             d = dist[v]
#             if np.isinf(d):
#                 return

#             for w in self.valves[v].neighbors:
#                 dist[w] = min(dist[w], d + 1)

#         return dist

#     def search(self, curr, unvisited, remaining=30, flow=0):
#         flows = [
#             self.search(
#                 valve,
#                 unvisited - {valve},
#                 rem,
#                 flow + self.valves[valve].flowrate * rem,
#             )
#             for valve in unvisited
#             for rem in [remaining - self.dist.loc[curr, valve] - 1]
#             if rem > 0
#         ]

#         return max([flow] + flows)

#     def most_pressure(self, start="AA"):

#         # print(unvisited)
#         # print("\n".join(map(str, self.valves.values())))
#         # print(self.dist)
#         return self.search(start, unvisited, remaining=30)

#     def neighbors(self, valve):
#         return [
#             valve,
#             unvisited - {valve},
#             rem,
#             flow + self.valves[valve].flowrate * rem,
#             for valve in unvisited
#             for rem in [remaining - self.dist.loc[curr, valve] - 1]
#             if rem > 0
#         ]

#     def search_n(self, curr, unvisited, remaining=26, flow=0):
#         max_relief = {}
#         queue = ["AA"]

#         while queue:
#             curr = queue.pop(0)
#             for valve in


# volcano = Volcano("day16.txt")

# print(volcano.most_pressure())
