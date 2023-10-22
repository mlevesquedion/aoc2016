import re


microchips = {}
generators = {}
for i, line in enumerate(open('day11.txt')):
    microchips |= {x: i for x in re.findall(r'a ([a-z]+)-compatible microchip', line)}
    generators |= {x: i for x in re.findall(r'a ([a-z]+) generator', line)}

INITIAL_PAIRS = [(microchips[element], generators[element]) for element in microchips]


def legal(pairs):
    for chip, generator in pairs:
        if chip != generator and any(chip == g2 for _, g2 in pairs):
            return False
    return True


def freeze(pairs):
    return tuple(map(tuple, sorted(pairs)))


def unfreeze(pairs):
    return list(map(list, pairs))


def maybe_add_next(Q, seen, floor, pairs):
    if not legal(pairs):
        return
    state = (floor, freeze(pairs))
    if state not in seen:
        Q.append(state)
        seen.add(state)


def min_steps(pairs):
    initial_floor = 0
    initial_pairs = freeze(pairs)
    Q = [(initial_floor, initial_pairs)]
    seen = set(Q)
    steps = 0
    while Q:
        next_Q = []
        for current_floor, pairs in Q:
            if all(x == 3 for p in pairs for x in p):
                return steps

            movable = []
            for pair_index, (chip_floor, generator_floor) in enumerate(pairs):
                if chip_floor == current_floor:
                    movable.append((pair_index, 0))
                if generator_floor == current_floor:
                    movable.append((pair_index, 1))

            floors = []
            if current_floor > 0:
                floors.append(current_floor-1)
            if current_floor < 3:
                floors.append(current_floor+1)

            for next_floor in floors:
                for pi, i in movable:
                    next_pairs = unfreeze(pairs)
                    next_pairs[pi][i] = next_floor
                    maybe_add_next(next_Q, seen, next_floor, next_pairs)
                    for pj, j in movable:
                        if (pi, i) == (pj, j):
                            continue
                        next_pairs = unfreeze(pairs)
                        next_pairs[pi][i] = next_floor
                        next_pairs[pj][j] = next_floor
                        maybe_add_next(next_Q, seen, next_floor, next_pairs)

        Q = next_Q
        steps += 1


print('part 1:', min_steps(INITIAL_PAIRS))
print('part 2:', min_steps(INITIAL_PAIRS + [(0, 0), (0, 0)]))
