part1 = 0
part2 = 0
for line in open('day07.txt'):
    i = 0
    in_brackets = False
    has_abba = False
    has_abba_in_brackets = False
    aba = set()
    bab = set()
    while i < len(line) - 2:
        if line[i] == '[':
            in_brackets = True
            i += 1
        if line[i] == ']':
            in_brackets = False
            i += 1
        if line[i] != line[i+1] and line[i] == line[i+2]:
            if in_brackets:
                aba.add(line[i:i+3])
            else:
                bab.add(line[i:i+3])
        if i < len(line) - 3 and line[i] != line[i+1] and line[i] == line[i+3] and line[i+1] == line[i+2]:
            if in_brackets:
                has_abba_in_brackets = True
            else:
                has_abba = True
        i += 1
    part1 += has_abba and not has_abba_in_brackets
    part2 += bool({b+a+b for a, b, _ in aba} & bab)

print('part 1:', part1)
print('part 2:', part2)
