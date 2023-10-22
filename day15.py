import itertools
import math
import re


discs = []
start_time, step = 0, 1
multiple = 1
for i, line in enumerate(open('day15.txt'), 1):
    _, positions, _, start = map(int, re.findall(r'\d+', line))
    discs.append((positions, start))
    if positions > step:
        start_time = - ((start + i) % positions)
        step = positions
    if ((start + i) % positions == 0) and positions > multiple:
        multiple = positions
step = math.lcm(step, multiple)


def find_time():
    for time in itertools.count(start_time, step):
        if all((start + time + i) % positions == 0 for i, (positions, start) in enumerate(discs, 1)):
            return time


print('part 1:', find_time())

discs.append((11, 0))
print('part 2:', find_time())
