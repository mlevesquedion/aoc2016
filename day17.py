import hashlib


shortest = None
longest = 0
Q = [(0, 0, '')]
for x, y, path in Q:
    if (x, y) == (3, 3):
        if shortest is None:
            shortest = path
        longest = max(longest, len(path))
        continue
    up, down, left, right, *_ = hashlib.md5(b'qljzarfv' + path.encode()).hexdigest()
    if up in 'bcdef' and y > 0:
        Q.append((x, y-1, path+'U'))
    if down in 'bcdef' and y < 3:
        Q.append((x, y+1, path+'D'))
    if left in 'bcdef' and x > 0:
        Q.append((x-1, y, path+'L'))
    if right in 'bcdef' and x < 3:
        Q.append((x+1, y, path+'R'))

print('part 1:', shortest)
print('part 2:', longest)
