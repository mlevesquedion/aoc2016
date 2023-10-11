import collections
import itertools
import re

# Pu, Pm, Ru, Sr, Tm, El, Dl
initial_state = tuple([0] + [0, 1] + [2, 2] + [2, 2] + [0, 1] + [0, 0] + [0, 0] + [0, 0])
want_state = tuple([3] * 15)

def legal(state):
    generators = {state[i] for i in range(1, 14, 2)}
    for generator, microchip in [state[i:i+2] for i in range(1, 14, 2)]:
        if generator != microchip and microchip in generators:
            return False
    return True

steps = 0
Q = [tuple(initial_state)]
seen = set(Q)
while Q:
    next_Q = []
    for state in Q:
        if state == want_state:
            break

        me = state[0]
        movable = [index+1 for (index, floor) in zip(range(14), state[1:]) if floor == me]
        candidate_states = []
        moves = ([-1] if me > 0 else []) + ([1] if me < 3 else [])
        for first in movable:
            for move in moves:
                next_state = list(state)
                next_state[0] += move
                next_state[first] += move
                candidate_states.append(tuple(next_state))
                for second in movable:
                    if first == second:
                        continue
                    next_state = list(state)
                    next_state[0] += move
                    next_state[first] += move
                    next_state[second] += move
                    candidate_states.append(tuple(next_state))
        for next_state in candidate_states:
            if legal(next_state) and next_state not in seen:
                next_Q.append(next_state)
                seen.add(next_state)

    if state == want_state:
        break

    Q = next_Q
    steps += 1
    print(steps, len(Q))

assert Q
print('part 2:', steps)
