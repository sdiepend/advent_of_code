with open("input") as f:
    content = f.readlines()

instructions = [int(x.strip()) for x in content]

steps = 0
pos = 0

while pos < len(instructions):
    old_pos = pos
    pos = pos + instructions[pos]
    instructions[old_pos] += 1
    steps += 1

print(steps)
