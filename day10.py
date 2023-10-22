import collections
import math
import re


bot_values = collections.defaultdict(list)
bot_children = {}
outputs = collections.defaultdict(list)
work = []
for line in open('day10.txt'):
    ints = [int(x) for x in re.findall(r'\d+', line)]
    if 'value' in line:
        value, bot = ints
        bot_values[bot].append(value)
        if len(bot_values[bot]) == 2:
            work.append(bot)
    else:
        bot, low, high = ints
        low_target = high_target = bot_values
        if f'output {low}' in line:
            low_target = outputs
        if f'output {high}' in line:
            high_target = outputs
        bot_children[bot] = (low_target, low, high_target, high)

while work:
    bot = work.pop()
    low_target, low, high_target, high = bot_children[bot]
    low_value, high_value = sorted(bot_values[bot])
    if low_value == 17 and high_value == 61:
        print('part 1:', bot)
    low_target[low].append(low_value)
    high_target[high].append(high_value)
    if len(low_target[low]) == 2:
        work.append(low)
    if len(high_target[high]) == 2:
        work.append(high)

print('part 2:', math.prod([outputs[i][0] for i in range(3)]))
