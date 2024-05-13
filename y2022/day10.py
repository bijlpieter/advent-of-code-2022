import numpy as np

class CPU:
	def __init__(self, fname):
		self.register = 1
		self.cycle = 0
		self.history = np.ones(240, dtype=int)

		with open(fname) as fp:
			instructions = fp.read().strip().split('\n')

		for instr in instructions:
			self.execute(instr)

	def execute(self, instr):
		self.history[self.cycle] = self.register
		self.cycle += 1
		
		op = instr.split(' ')
		if op[0] == "addx":
			self.history[self.cycle] = self.register
			
			arg = int(op[1])
			self.register += arg
			self.cycle += 1

	def get_history(self):
		return self.history.reshape(6, 40)

cpu = CPU("day10.txt")
history = cpu.get_history()
weights = np.arange(20, 240, 40)

print(f"Part 1: {history[:, 19] @ weights}")

pixels = np.where(np.abs(history - np.arange(40)) <= 1, "#", ".")
print(f"Part 2:")
print('\n'.join("".join(i) for i in pixels))
