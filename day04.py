import collections
import string


total = 0
for line in open('day04.txt'):
    line = line.replace('-', '')

    checksum_start = line.index('[')
    sector_id = int(line[checksum_start-3:checksum_start])
    checksum = line[checksum_start+1:checksum_start+6]
    letters = line[:checksum_start-3]
    counts = collections.Counter(letters)

    checksum_letters = []
    for letter, count in sorted(counts.most_common(), key=lambda lettercount: (lettercount[1], -ord(lettercount[0])), reverse=True):
        checksum_letters.append(letter)
        if len(checksum_letters) == 5:
            break

    if checksum == ''.join(checksum_letters):
        total += sector_id
print('part 1:', total)

for line in open('day04.txt'):
    checksum_start = line.index('[')
    sector_id = int(line[checksum_start-3:checksum_start])
    letters = line[:checksum_start-3]

    shift = sector_id % 26
    translator = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift])
    translated = letters.translate(translator)

    if all(word in translated for word in 'north pole object'.split()):
        print('part 2:', sector_id)
