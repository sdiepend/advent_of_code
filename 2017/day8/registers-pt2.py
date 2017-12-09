import operator

with open("input") as f:
    content = f.readlines()

instructions = [x.strip().split(' ') for x in content]

ops = {'>': operator.gt,
       '<': operator.lt,
       '>=': operator.ge,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       'inc': operator.add,
       'dec': operator.sub}


registers = {}
highest = 0

for instruction in instructions:
    instr_key = instruction[0]
    instr_op = instruction[1]
    instr_val = int(instruction[2])
    cond_key = instruction[4]
    cond_op = instruction[5]
    cond_val = int(instruction[6])
    
    if instr_key not in registers:
        registers[instr_key] = 0
    if cond_key not in registers:
        registers[cond_key] = 0
    if ops[cond_op](registers[cond_key], cond_val):
        registers[instr_key] = ops[instr_op](registers[instr_key], instr_val)
    temp_max = max(registers.values())
    if temp_max > highest:
        highest = temp_max
    
print(highest)
