SET, MOV, INC, DEC, JMP, JNZ = range(6)


def simulate(c):
    pc = 0
    registers = [0, 0, c, 0]
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
        pc += 1
    return registers[0]


register_index = 'abcd'.index
code = []
for line in list(open('day12.txt')):
    parts = line.split()
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
                if parts[1] != '0':
                    code.append((JMP, int(parts[2])))
            else:
                code.append((JNZ, register_index(parts[1]), int(parts[2])))

print('part 1:', simulate(0))
print('part 2:', simulate(1))
