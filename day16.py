def dragon(data, disk_length):
    while len(data) < disk_length:
        data = data + '0' + ''.join(['01'[x == '0'] for x in data[::-1]])
    data = data[:disk_length]
    checksum = data
    while True:
        chunks = [checksum[i:i+2] for i in range(0, len(checksum)-1, 2)]
        checksum = ''.join('01'[a == b] for a, b in chunks)
        if len(checksum) % 2:
            break
    return checksum


data = '00101000101111010'
print('part 1:', dragon(data, 272))
print('part 2:', dragon(data, 35651584))
