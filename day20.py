ranges = sorted([tuple(map(int, line.split('-'))) for line in open('day20.txt')])


def part1():
    low = 0
    for range_low, range_high in ranges:
        if low < range_low:
            return low
        low = max(low, range_high + 1)


print('part 1:', part1())


def part2():
    low = 0
    count = 0
    for range_low, range_high in ranges:
        count += max(range_low - low, 0)
        low = max(low, range_high + 1)
    return count


print('part 2:', part2())
