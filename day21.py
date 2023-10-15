import re


FIRST_PASSWORD = 'abcdefgh'
SECOND_PASSWORD = 'fbgdceah'
PASSWORD_LENGTH = len(FIRST_PASSWORD)
INSTRUCTIONS = list(open('day21.txt'))


def rotation_amount(i):
    return (1 + i + (1 if i >= 4 else 0)) % PASSWORD_LENGTH


rotation_inverse = {(i + rotation_amount(i)) % PASSWORD_LENGTH: i for i in range(PASSWORD_LENGTH)}

REVERSED_INSTRUCTIONS = []
for line in INSTRUCTIONS:
    if line.startswith('rotate based'):
        REVERSED_INSTRUCTIONS.append('invert ' + line)
    elif line.startswith('rotate left'):
        REVERSED_INSTRUCTIONS.append(line.replace('left', 'right'))
    elif line.startswith('rotate right'):
        REVERSED_INSTRUCTIONS.append(line.replace('right', 'left'))
    elif line.startswith('move'):
        i, j =  re.findall('\d+', line)
        REVERSED_INSTRUCTIONS.append(f'move position {j} to position {i}')
    # swaps and reverse are their own inverses
    else:
        REVERSED_INSTRUCTIONS.append(line)
REVERSED_INSTRUCTIONS.reverse()


def scramble(password, instructions):
    password = list(password)
    for line in instructions:
        if line.startswith('swap position'):
            i, j = map(int, re.findall('\d+', line))
            password[i], password[j] = password[j], password[i]
        elif line.startswith('swap letter'):
            a, b = re.findall('letter ([a-z])', line)
            i, j = password.index(a), password.index(b)
            password[i], password[j] = password[j], password[i]
        elif line.startswith('rotate based'):
            letter = line[-2]
            index = password.index(letter)
            rotation = rotation_amount(index)
            password = password[-rotation:] + password[:-rotation]
        elif line.startswith('invert rotate'):
            letter = line[-2]
            index = password.index(letter)
            want_index = rotation_inverse[index]
            rotation = index - want_index
            password = password[rotation:] + password[:rotation]
        elif line.startswith('rotate'):
            _, direction, amount, _ = line.split()
            rotation = int(amount) % PASSWORD_LENGTH
            if direction == 'right':
                rotation *= -1
            password = password[rotation:] + password[:rotation]
        elif line.startswith('reverse'):
            i, j = map(int, re.findall('\d+', line))
            password = password[:i] + password[i:j+1][::-1] + password[j+1:]
        elif line.startswith('move'):
            i, j = map(int, re.findall('\d+', line))
            letter = password.pop(i)
            password.insert(j, letter)
    return ''.join(password)


print('part 1:', scramble(FIRST_PASSWORD, INSTRUCTIONS))
print('part 2:', scramble(SECOND_PASSWORD, REVERSED_INSTRUCTIONS))
