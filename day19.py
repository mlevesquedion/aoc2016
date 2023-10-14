import math

n = 3004953


def josephus(n):
    return 2 * (n - 2**(int(math.log(n, 2)))) + 1


print('part 1:', josephus(n))


def part2(n):
    # derived this relationship by examining outputs from a naive implementation
    previous_pow3 = 3**int(math.log(n, 3))
    result = n - previous_pow3
    if result > previous_pow3:
        result += (result - previous_pow3)
    return result


print('part 2:', part2(n))
