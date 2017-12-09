with open("input") as f:
    content = f.readlines()

instructions = [int(x.strip()) for x in content]

# instructions = [0, 3, 0, 1, -3]
steps = 0
pos = 0

while pos < len(instructions) and pos >= 0:
    old_pos = pos
    pos = pos + instructions[pos]
    if instructions[old_pos] >= 3:
        instructions[old_pos] -= 1
    else:
        instructions[old_pos] += 1
    steps += 1

print(steps)
