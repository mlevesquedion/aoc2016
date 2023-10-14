FAVORITE_NUMBER = 1362
TARGET = (31, 39)


# I tried optimizing by using bit operations and functools.cache, but neither seems to help
def is_open(x, y):
    return sum(bit == '1' for bit in bin(x*x + 3*x + 2*x*y + y + y*y + FAVORITE_NUMBER)[2:]) % 2 == 0


start = (1, 1)
Q = [start]
seen = set(Q)
steps = 0
target_steps = None
reachable_in_50 = None
while target_steps is None or reachable_in_50 is None:
    next_Q = []

    for x, y in Q:
        if (x, y) == TARGET:
            target_steps = steps
        left, right, up, down = (x-1, y), (x+1, y), (x, y-1), (x, y+1)
        for neighbor in (left, right, up, down):
            if x == 0 and neighbor == left or y == 0 and neighbor == up:
                continue
            if is_open(*neighbor) and neighbor not in seen:
                next_Q.append(neighbor)
                seen.add(neighbor)

    Q = next_Q
    steps += 1
    if steps == 50:
        reachable_in_50 = len(seen)

print('part 1:', target_steps)
print('part 2:', reachable_in_50)
