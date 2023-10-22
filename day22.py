import itertools
import re
import sys


nodes = 0
max_x = max_y = 0
big = set()
empty = None
for line in itertools.islice(open('day22.txt'), 2, sys.maxsize):
    x, y, size, used, *_ = map(int, re.findall(r'\d+', line))
    nodes += 1
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    if size > 500:
        big.add((x, y))
    if used == 0:
        empty = (x, y)
print('part 1:', nodes - len(big) - 1)

Q = [empty]
steps = 0
seen = set(Q)
while Q:
    next_Q = []

    for x, y in Q:
        if (x, y) == (max_x, 0):
            # Move the empty node to the bottom left of the target data which
            # takes (steps - 2) moves, then move the target data all the way left.
            # When the empty node is bottom left of the target data, moving 
            # the target data left 1 unit and repositioning the empty node takes 5 moves.
            # For the last move, we don't need to reposition the empty node so it takes 2 moves.
            print('part 2:', steps + 5*(max_x-1))
            exit()
        for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if not 0 <= nx <= max_x or not 0 <= ny <= max_y or (nx, ny) in big:
                continue
            if (nx, ny) in seen:
                continue
            seen.add((nx, ny))
            next_Q.append((nx, ny))

    Q = next_Q
    steps += 1
