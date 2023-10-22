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
    keycount = 0
    candidate_keys = collections.defaultdict(list)
    while True:
        digest = hash_function(SALT + str(i).encode())
        for quintuple in list(candidate_keys):
            if quintuple in digest:
                for ci, _ in candidate_keys[quintuple]:
                    keycount += 1
                    if keycount == 64:
                        return ci
                del candidate_keys[quintuple]
            candidate_keys[quintuple] = [(ci, expiration) for (ci, expiration) in candidate_keys[quintuple] if expiration > i]
            if not candidate_keys[quintuple]:
                del candidate_keys[quintuple]
        for j in range(0, len(digest)-2, 1):
            if digest[j] == digest[j+1] == digest[j+2]:
                candidate_keys[digest[j]*5].append((i, i+1000))
                break
        i += 1


print('part 1:', find_index(md5))
print('part 2:', find_index(md5_stretched))
