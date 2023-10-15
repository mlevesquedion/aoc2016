import math


# I analyzed the code, translated it to Python and simplified it. The trickiest
# bit is the tgl instruction. Thankfully, the code only contains one, and it's
# possible to see it will run a-1 times, at offsets 2*(a-2), 2*(a-3), etc. 
# until 2. Some of those may be out of bounds due to the initial value of a. 
# The last offset will be 2, because that will change `jnz 1 c` into `cpy 1 c`, 
# causing execution to fall through and never hit the tgl instruction again.
def compute(start):
    return math.factorial(start) + 6460


print('part 1:', compute(7))
print('part 2:', compute(12))
