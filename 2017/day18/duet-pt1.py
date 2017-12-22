def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def play(instructions):
    registers = {}
    last_played = 0
    i = 0
    while 0 <= i < len(instructions):
        instr = instructions[i]
        oper = instr[0]
        reg_key = instr[1]

        if len(instr) == 3:
            if is_number(instr[2]):
                val = int(instr[2])
            else:
                val = int(registers[instr[2]])

        if reg_key not in registers.keys():
            registers[reg_key] = 0

        if oper == 'set':
            registers[reg_key] = val
            i += 1
        elif oper == 'add':
            registers[reg_key] = registers[reg_key] + val
            i += 1
        elif oper == 'mul':
            registers[reg_key] = registers[reg_key] * val
            i += 1
        elif oper == 'mod':
            registers[reg_key] = registers[reg_key] % val
            i += 1
        elif oper == 'snd':
            last_played = registers[reg_key]
            i += 1
        elif oper == 'jgz':
            if is_number(reg_key):
                if reg_key > 0:
                    i = i + val
                else:
                    i += 1
            elif registers[reg_key] > 0:
                i = i + val
            else:
                i += 1
        elif oper == 'rcv':
            if registers[reg_key] != 0:
                registers[reg_key] = last_played
                return last_played
            i += 1

if __name__ == "__main__":
    with open('input') as f:
        content = f.readlines()

    instructions = [x.strip().split() for x in content]
    
    print(play(instructions))
