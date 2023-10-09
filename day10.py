import collections
import math
import re

bots = collections.defaultdict(lambda: [[], (None, None)])
work = []
for line in open('day10.txt'):
    ints = [int(x) for x in re.findall('\d+', line)]
    if 'value' in line:
        chip, target = ints
        bots[target][0].append(chip)
        if len(bots[target][0]) == 2:
            work.append(target)
    else:
        target, lo, hi = ints
        if f'output {lo}' in line:
            lo = str(lo)
        if f'output {hi}' in line:
            hi = str(hi)
        bots[target][1] = (lo, hi)

outs = {}
while work:
    bot = work.pop()
    chips, (lo, hi) = bots[bot]
    lo_chip, hi_chip = sorted(chips)
    if lo_chip == 17 and hi_chip == 61:
        print('part 1:', bot)
    if isinstance(lo, str):
        outs[lo] = lo_chip
    else:
        bots[lo][0].append(lo_chip)
        if len(bots[lo][0]) == 2:
            work.append(lo)
    if isinstance(hi, str):
        outs[hi] = hi_chip
    else:
        bots[hi][0].append(hi_chip)
        if len(bots[hi][0]) == 2:
            work.append(hi)

print('part 2:', math.prod([outs[i] for i in '012']))
