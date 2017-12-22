import re
with open('input') as f:
    content = f.readline()

moves = content.strip().split(',')

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] 

for move in moves:
    if move[0] == 's':
        shift = int(re.sub(r's([0-9]+)', r'\1', move)) % len(programs)
        programs = programs[len(programs)-shift:] + programs[:len(programs)-shift]
    if move[0] == 'x':
        pos_a = int(re.sub(r'x([0-9]+)/[0-9]+', r'\1', move))
        pos_b = int(re.sub(r'x[0-9]+/([0-9]+)', r'\1', move))
        a = programs[pos_a]
        b = programs[pos_b]
        programs[pos_a] = b
        programs[pos_b] = a
    if move[0] == 'p':
        prog_one = re.sub(r'p([a-z])/[a-z]', r'\1', move)
        prog_two = re.sub(r'p[a-z]/([a-z])', r'\1', move)
        prog_one_index = programs.index(prog_one)
        prog_two_index = programs.index(prog_two)
        programs[prog_one_index] = prog_two
        programs[prog_two_index] = prog_one

programs_string = ''
for letter in programs:
    programs_string += letter

print(programs_string)
