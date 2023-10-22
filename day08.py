import itertools
import re


screen = [['.' for _ in range(50)] for _ in range(6)]

for line in open('day08.txt'):
    ints = [int(x) for x in re.findall(r'\d+', line)]
    if 'rect' in line:
        for x, y in itertools.product(range(ints[0]), range(ints[1])):
            screen[y][x] = '#'
    if 'row' in line:
        y, rotation = ints
        screen[y] = screen[y][-rotation:] + screen[y][:-rotation]
    if 'column' in line:
        x, rotation = ints
        column = [row[x] for row in screen]
        column = column[-rotation:] + column[:-rotation]
        for y in range(len(screen)):
            screen[y][x] = column[y]

print('part 1:', sum(sum(cell == '#' for cell in row) for row in screen))
print('part 2:')
print('\n'.join(map(''.join, screen)))
