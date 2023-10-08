instructions = [(line[0], int(line[1:])) for line in open('day01.txt').read().split(', ')]

RIGHT_TURN = dict(zip('NESW', 'ESWN'))
LEFT_TURN = dict(zip('NWSE', 'WSEN'))
DIRECTION_DELTA = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}


def blocks_away(position):
    return sum(map(abs, position))


first_visited_twice = None
direction = 'N'
position = (0, 0)
visited = set(position)

for turn, blocks in instructions:
    match turn:
        case 'L':
            direction = LEFT_TURN[direction]
        case 'R':
            direction = RIGHT_TURN[direction]
    delta = DIRECTION_DELTA[direction]
    for _ in range(blocks):
        position = (position[0] + delta[0], position[1] + delta[1])
        if position in visited and first_visited_twice is None:
            first_visited_twice = position
        visited.add(position)

print('part 1:', blocks_away(position))
print('part 2:', blocks_away(first_visited_twice))
