Interval = tuple[int, int]
Coord = tuple[int, int]
Dist = int

def manhattan(a: Coord, b: Coord) -> Dist:
	x1, y1 = a
	x2, y2 = b
	return abs(x1 - x2) + abs(y1 - y2)

def interval(sensor: Coord, dist: Dist, y: int) -> Interval | None:
	sx, sy = sensor
	dx = dist - abs(sy - y)
	return (sx - dx, sx + dx) if dx >= 0 else None

def get_intervals(sensors: list[Coord], beacons: list[Coord], y: int) -> list[Interval]:
	return [
		interval(
			sensor, 
			manhattan(sensor, beacon),
			y=y
		)
		for sensor, beacon in zip(sensors, beacons)
	]

def merge_intervals(intervals: list[Interval]) -> list[Interval]:
	unmerged = sorted(intervals, key=lambda x: x[0])
	merged = [unmerged[0]]

	for i_left, i_right in unmerged:
		p_left, p_right = merged[-1]
		if i_left <= p_right:
			n_right = max(p_right, i_right)
			merged[-1] = (p_left, n_right)
		else:
			merged.append((i_left, i_right))

	return merged

def interval_len(interval: Interval) -> int:
	left, right = interval
	return right - left + 1

def in_intervals(intervals: list[Interval], val: int) -> bool:
	return any(left <= val <= right for left, right in intervals)

def no_beacons(sensors, beacons, y):
	intervals = get_intervals(sensors, beacons, y)
	intervals = [interval for interval in intervals if interval is not None]
	intervals = merge_intervals(intervals)

	total_len = sum(interval_len(interval) for interval in intervals)
	counted_beacons = sum(in_intervals(intervals, bx) for bx, by in set(beacons) if by == y)

	return total_len - counted_beacons

def find_distress_beacon(sensors, beacons):
	for y in range(4000001):
		intervals = get_intervals(sensors, beacons, y)
		intervals = [interval for interval in intervals if interval is not None]
		intervals = merge_intervals(intervals)

		if len(intervals) != 1:
			x = intervals[0][1] + 1
			return x * 4000000 + y

with open("day15.txt") as fp:
	lines = fp.readlines()

sensors = [(int(a[2:-1]), int(b[2:-1])) for line in lines for a, b in [line.split(" ")[2:4]]]
beacons = [(int(a[2:-1]), int(b[2:-1])) for line in lines for a, b in [line.split(" ")[8:]]]

print(f"Part 1: {no_beacons(sensors, beacons, y=2000000)}")
print(f"Part 2: {find_distress_beacon(sensors, beacons)}")
