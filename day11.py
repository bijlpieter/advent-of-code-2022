import operator
import numpy as np

def get_operation(op_str):
	ops = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.floordiv
	}

	left, op, right = op_str.split(" ")

	return lambda x: ops[op](x if left == "old" else int(left), x if right == "old" else int(right))

class Monkey:
	def __init__(self, mstr, pack):
		(
			monkey_id,
			start,
			operation,
			test,
			iftrue,
			iffalse
		) = mstr.split("\n")

		self.id = monkey_id[7:-1]
		self.items = [int(item) for item in start[18:].split(", ")]
		self.op = get_operation(operation[19:])
		self.test = int(test[21:])

		self.throw = [
			iffalse[30:],
			iftrue[29:]
		]

		self.pack = pack
		self.inspections = 0

	def catch_item(self, item):
		self.items.append(item)

	def do_turn(self, do_div=0, do_mod=0):
		self.inspections += len(self.items)
		while self.items:
			item = self.items.pop(0)
			if do_mod:
				item %= do_mod
			item = self.op(item)
			if do_div:
				item //= do_div
			throw_to = self.throw[item % self.test == 0]
			self.pack[throw_to].catch_item(item)

class Pack:
	def __init__(self, fname):
		with open(fname) as fp:
			monkeys = fp.read().strip().split("\n\n")

		self.pack = {}
		for mstr in monkeys:
			monkey = Monkey(mstr, self.pack)
			self.pack[monkey.id] = monkey

	def do_rounds(self, n=1, do_div=0, do_mod=0, print_every=0):
		for i in range(n):
			for monkey_id, monkey in self.pack.items():
				monkey.do_turn(do_div, do_mod)

			nr = i+1
			if print_every and nr % print_every == 0:
				self.print(round_nr=nr)

	def print(self, round_nr):
		print(f"== After round {round_nr} ==")
		for monkey_id, monkey in self.pack.items():
			print(f"Monkey {monkey_id}: inspected: {monkey.inspections} items:{monkey.items}")

	def get_most_active(self, n=2):
		return sorted([monkey.inspections for monkey in self.pack.values()])[-n:]

	def get_modulus(self):
		return int(np.prod([monkey.test for monkey in self.pack.values()]))


pack = Pack("day11.txt")
pack.do_rounds(n=20, do_div=3)
one, two = pack.get_most_active()
print(f"Part 1: {one * two}")

pack = Pack("day11.txt")
mod = pack.get_modulus()
pack.do_rounds(n=10000, do_mod=mod)
one, two = pack.get_most_active()
print(f"Part 2: {one * two}")
