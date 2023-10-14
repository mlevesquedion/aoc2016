chars = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
row = mask = 0
for c in chars:
    row = (row << 1) | (c == '^')
    mask = (mask << 1) | 1

count = 0
part1 = 0
for i in range(400_000):
    if i == 40:
        part1 = count
    count += (row ^ mask).bit_count()
    row = ((row << 1) ^ (row >> 1)) & mask
    
print('part 1:', part1)
print('part 2:', count)
