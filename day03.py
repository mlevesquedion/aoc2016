import itertools


def possible(triangle):
    a, b, c = sorted(triangle)
    return a + b > c


triangles = [tuple(map(int, line.split())) for line in open('day03.txt')]

vertical_triangles = itertools.batched(itertools.chain(*zip(*triangles)), 3)

print('part 1:', sum(map(possible, triangles)))
print('part 2:', sum(map(possible, vertical_triangles)))
