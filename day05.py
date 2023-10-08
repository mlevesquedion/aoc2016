import hashlib

seed = b'uqwqemis'

i = 0
chars = []
remaining_positions = set('01234567')
positions = [None] * 8
while remaining_positions:
        m = hashlib.md5()
        m.update(seed)
        m.update(str(i).encode())
        digest = m.hexdigest()
        if digest[:5] == '00000':
            if len(chars) < 8:
                chars.append(digest[5])
            if digest[5] in remaining_positions:
                positions[int(digest[5])] = digest[6]
                remaining_positions.remove(digest[5])
        i += 1

print('part 1:', ''.join(chars))
print('part 2:', ''.join(positions))
