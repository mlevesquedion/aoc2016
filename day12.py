def fib(n):
    sqrt5 = 5**0.5
    phi = (1+sqrt5)/2
    return round(phi**n/sqrt5)


# I analyzed the code and converted it to Python.
def simulate(c):
    d = 26
    if c:
        d += 7
    return fib(d+2) + 209


print('part 1:', simulate(0))
print('part 2:', simulate(1))
