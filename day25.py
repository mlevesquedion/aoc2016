SET, MOV, INC, DEC, JMP, JNZ, NOP, OUT = range(8)

 
code = []
register_index = 'abcd'.index
for parts in [line.split() for line in open('day25.txt')]:
    match parts[0]:
        case 'cpy':
            if parts[1].isdigit():
                code.append((SET, int(parts[1]), register_index(parts[2])))
            else:
                code.append((MOV, register_index(parts[1]), register_index(parts[2])))
        case 'inc':
            code.append((INC, register_index(parts[1])))
        case 'dec':
            code.append((DEC, register_index(parts[1])))
        case 'jnz':
            if parts[1].isdigit():
                if parts[1] == '0':
                    code.append((NOP,))
                else:
                    code.append((JMP, int(parts[2])))
            else:
                code.append((JNZ, register_index(parts[1]), int(parts[2])))
        case 'out':
            code.append((OUT, register_index(parts[1])))


def simulate(i):
    out = []
    registers = [i, 0, 0, 0]
    pc = 0
    while pc < len(code):
        instruction = code[pc]
        if instruction[0] == SET:
            registers[instruction[2]] = instruction[1]
        elif instruction[0] == MOV:
            registers[instruction[2]] = registers[instruction[1]]
        elif instruction[0] == INC:
            registers[instruction[1]] += 1
        elif instruction[0] == DEC:
            registers[instruction[1]] -= 1
        elif instruction[0] == JMP:
            pc += instruction[1]
            continue
        elif instruction[0] == JNZ:
            if registers[instruction[1]]:
                pc += instruction[2]
                continue
        elif instruction[0] == OUT:
            out.append(registers[instruction[1]])
            if tuple(out) == (0, 1, 0, 1, 0, 1, 0, 1):
                return i
            if len(out) == 8:
                return None
        # fallthrough for NOP
        pc += 1



i = 1
while True:
    if simulate(i):
        print('part 1:', i)
        break
    i += 1
