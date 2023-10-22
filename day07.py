part1 = 0
part2 = 0
for line in open('day07.txt'):
    i = 0
    in_brackets = False
    has_abba = False
    has_abba_in_brackets = False
    ab = set()
    ba = set()
    for i in range(len(line) - 3):
        if line[i] == '[':
            in_brackets = True
            continue
        elif line[i] == ']':
            in_brackets = False
            continue
        elif line[i] != line[i+1]:
            if line[i] == line[i+2]:
                if in_brackets:
                    ab.add(line[i:i+2])
                else:
                    ba.add(line[i:i+2])
            elif line[i] == line[i+3] and line[i+1] == line[i+2]:
                if in_brackets:
                    has_abba_in_brackets = True
                else:
                    has_abba = True
    part1 += has_abba and not has_abba_in_brackets
    part2 += any(b+a in ba for a, b in ab)

print('part 1:', part1)
print('part 2:', part2)
