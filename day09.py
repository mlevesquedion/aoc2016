import math

total = 0
for line in open('day09.txt'):
    i = 0
    while i < len(line):
        if line[i] == '(':
            count_end = i + 1
            while line[count_end] != 'x':
                count_end += 1
            count = int(line[i+1:count_end])
            times_end = count_end + 1
            while line[times_end] != ')':
                times_end += 1
            times = int(line[count_end+1:times_end])
            total += count * times
            i = times_end + 1 + count
        else:
            total += 1
            i += 1
print('part 1:', total)

# keep a running list of active "multipliers", with their respective remaining "lifetime"
# a given character is repeated a number of times equal to the product of the active multipliers
total = 0
for line in open('day09.txt'):
    i = 0
    multipliers = []
    while i < len(line):
        if line[i] == '(':
            count_end = i + 1
            while line[count_end] != 'x':
                count_end += 1
            count = int(line[i+1:count_end])
            times_end = count_end + 1
            while line[times_end] != ')':
                times_end += 1
            times = int(line[count_end+1:times_end])
            multipliers = [(new_life, mul) for life, mul in multipliers if (new_life := life - (times_end - i + 1)) > 0]
            multipliers.append((count, times))
            i = times_end + 1
        else:
            total += math.prod([mul for _, mul in multipliers])
            multipliers = [(new_life, mul) for life, mul in multipliers if (new_life := life - 1) > 0]
            i += 1
print('part 2:', total)
