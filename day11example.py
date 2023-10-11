import itertools
import re

ME, HG, HM, LG, LM = range(5)
initial_state = (0, 1, 0, 2, 0)

want_state = (3, 3, 3, 3, 3)

def legal(state):
    me, hg, hm, lg, lm = state
    if hm != hg and hm == lg:
        return False
    if lm != lg and lm == hg:
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
        movable = [index+1 for (index, floor) in zip(range(4), state[1:]) if floor == me]
        candidate_states = []
        for first in movable:
            moves = ([-1] if me > 0 else []) + ([1] if me < 3 else [])
            for move in moves:
                if move == -1 and first in {1, 3}:
                    continue
                next_state = list(state)
                next_state[0] += move
                next_state[first] += move
                candidate_states.append(tuple(next_state))
                for second in movable:
                    if move == -1 and second in {1, 3}:
                        continue
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

assert Q
print('part 1:', steps)
