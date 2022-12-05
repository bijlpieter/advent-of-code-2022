import numpy as np
import pandas as pd

class SupplyStacks:
    def __init__(self, fname):
        with open(fname) as fp:
            stack, instructions = fp.read().split("\n\n")

        layers = stack.split("\n")[::-1]
        self.stack = [
            [
                layer[i]
                for layer in layers[1:]
                if layer[i] != ' '
            ]
            for i in range(1, len(layers[0]), 4)
        ]

        self.instructions = [
            [int(x) for x in instr.split()[1::2]]
            for instr in instructions.strip().split("\n")
        ]

    def execute(self, start, end, count, order=-1):
        self.stack[start], to_move = self.stack[start][:-count], self.stack[start][-count:]
        self.stack[end] += to_move[::order]

    def solution(self):
        return "".join(x[-1] for x in self.stack)

    def run(self, order=-1):
        for count, start, end in self.instructions:
            self.execute(start-1, end-1, count, order)

        return self.solution()

supply_stacks = SupplyStacks("day05.txt")
print(f"Part 1: {supply_stacks.run(order=-1)}")

supply_stacks = SupplyStacks("day05.txt")
print(f"Part 2: {supply_stacks.run(order=1)}")
