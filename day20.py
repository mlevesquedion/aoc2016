ranges = sorted([tuple(map(int, line.split('-'))) for line in open('day20.txt')])

low = 0
first = None
count = 0
for range_low, range_high in ranges:
    if low < range_low and first is None:
        first = low
    count += max(range_low - low, 0)
    low = max(low, range_high + 1)

print('part 1:', first)
print('part 2:', count)
