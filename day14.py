import collections
import hashlib


SALT = b'cuanljph'


def md5(bytestring):
    return hashlib.md5(bytestring).hexdigest()


def md5_stretched(bytestring):
    for _ in range(2017):
        bytestring = md5(bytestring).encode()
    return bytestring.decode()


def find_index(hash_function):
    i = 0
    keys = 0
    candidates = collections.defaultdict(list)
    while True:
        digest = hash_function(SALT + str(i).encode())
        for c in list(candidates):
            if c in digest:
                for ci, _ in candidates[c]:
                    keys += 1
                    if keys == 64:
                        return ci
                del candidates[c]
            candidates[c] = [(ci, count-1) for (ci, count) in candidates[c] if count-1 > 0]
        for j in range(0, len(digest)-2, 1):
            if len(set(digest[j:j+3])) == 1:
                candidates[digest[j]*5].append((i, 1000))
                break
        i += 1


print('part 1:', find_index(md5))
print('part 2:', find_index(md5_stretched))
