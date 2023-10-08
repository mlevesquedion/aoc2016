import re

screen = [['.' for _ in range(50)] for _ in range(6)]

for line in open('day08.txt'):
    ints = [int(x) for x in re.findall('\d+', line)]
    if 'rect' in line:
        for y in range(ints[1]):
            for x in range(ints[0]):
                screen[y][x] = '#'
    if 'row' in line:
        y, by = ints
        screen[y] = screen[y][-by:] + screen[y][:-by]
    if 'column' in line:
        x, by = ints
        column = [row[x] for row in screen]
        column = column[-by:] + column[:-by]
        for y in range(len(screen)):
            screen[y][x] = column[y]

print('part 1:', sum(sum(cell == '#' for cell in row) for row in screen))
print('part 2:')
print('\n'.join(map(''.join, screen)))
