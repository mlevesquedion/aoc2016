import collections

most_common = [collections.Counter(row).most_common() for row in zip(*open('day06.txt'))]
print('part 1:', ''.join(mc[0][0] for mc in most_common))
print('part 2:', ''.join(mc[-1][0] for mc in most_common))
