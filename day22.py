import itertools
import re
import sys

import matplotlib.pyplot as plt

nodes = []
max_x = max_y = 0
big = set()
empty = None
for line in itertools.islice(open('day22.txt'), 2, sys.maxsize):
    x, y, size, used, avail, _ = map(int, re.findall(r'\d+', line))
    nodes.append((x, y, size, used, avail))
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    if size > 500:
        big.add((x, y))
    if used == 0:
        empty = (x, y)
print('part 1:', len(nodes) - len(big) - 1)

target = (max_x, 0)
Q = [(empty, target)]
steps = 0
seen = set(Q)
while Q:
    next_Q = []

    for (ex, ey), (tx, ty) in Q:
        if (tx, ty) == (0, 0):
            print('part 2:', steps)
            exit()
        for (nex, ney) in [(ex-1, ey), (ex+1, ey), (ex, ey-1), (ex, ey+1)]:
            if nex < 0 or nex > max_x or ney < 0 or ney > max_y or (nex, ney) in big:
                continue
            ntx, nty = tx, ty
            if (nex, ney) == (tx, ty):
                ntx, nty = ex, ey
            state = ((nex, ney), (ntx, nty))
            if state in seen:
                continue
            seen.add(state)
            next_Q.append(state)

    Q = next_Q
    steps += 1
