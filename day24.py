import itertools


number_positions = {}
grid = []
for y, line in enumerate(open('day24.txt')):
    row = list(line.strip())
    grid.append(row)
    for x, value in enumerate(row):
        if value.isdigit():
            number_positions[value] = (x, y)

distance_from_to = {}
for number, (x, y) in number_positions.items():
    distances = {}
    Q = [(x, y)]
    seen = set((x, y))
    distance = 0
    while Q:
        next_Q = []
        for x, y in Q:
            value = grid[y][x]
            if value.isdigit() and value != number:
                distances[value] = distance
            for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid) or grid[ny][nx] == '#' or (nx, ny) in seen:
                    continue
                seen.add((nx, ny))
                next_Q.append((nx, ny))
        Q = next_Q
        distance += 1
    distance_from_to[number] = distances

min_distance_p1 = min_distance_p2 = float('inf')
for path in itertools.permutations(sorted(distance_from_to)[1:]):
    distance = 0
    src = '0'
    for dst in path:
        distance += distance_from_to[src][dst]
        src = dst
    min_distance_p1 = min(min_distance_p1, distance)
    min_distance_p2 = min(min_distance_p2, distance + distance_from_to[src]['0'])

print('part 1:', min_distance_p1)
print('part 2:', min_distance_p2)
