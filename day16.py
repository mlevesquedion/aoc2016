import itertools


def dragon(data, disk_length):
    disk = [int(c) for c in data]
    while len(disk) < disk_length:
        disk.append(0)
        disk.extend([1-b for b in reversed(disk)])
    checksum = disk[:disk_length]
    while True:
        checksum = [a == b for a, b in itertools.batched(checksum, 2)]
        if len(checksum) % 2:
            break
    return ''.join('01'[b] for b in checksum)


data = '00101000101111010'
print('part 1:', dragon(data, 272))
print('part 2:', dragon(data, 35651584))
