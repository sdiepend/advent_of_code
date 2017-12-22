from collections import deque

with open('input') as f:
    content = f.readlines()

instructions = [x.strip().split() for x in content]

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def run(pg_pos, register, queue_snd, queue_rcv, count_snd):
    while 0 <= pg_pos < len(instructions):
        instr = instructions[pg_pos]
        oper = instr[0]
        reg_key = instr[1]
        print(oper)
        if len(instr) == 3:
            if is_number(instr[2]):
                val = int(instr[2])
            else:
                val = int(register[instr[2]])

        if reg_key not in register.keys():
            register[reg_key] = 0

        if oper == 'set':
            register[reg_key] = val
            pg_pos += 1
        elif oper == 'add':
            register[reg_key] = register[reg_key] + val
            pg_pos += 1
        elif oper == 'mul':
            register[reg_key] = register[reg_key] * val
            pg_pos += 1
        elif oper == 'mod':
            register[reg_key] = register[reg_key] % val
            pg_pos += 1
        elif oper == 'jgz':
            if is_number(reg_key):
                if int(reg_key) > 0:
                    pg_pos = pg_pos + int(reg_key)
                else:
                    pg_pos += 1
            elif register[reg_key] > 0:
                pg_pos = pg_pos + val
            else:
                pg_pos += 1
        elif oper == 'snd':
            print("put on " + str(queue_snd))
            if is_number(reg_key):
                queue_snd.append(int(reg_key))
            else:
                queue_snd.append(register[reg_key])
            pg_pos += 1
            count_snd += 1
        elif oper == 'rcv':
            try:
                register[reg_key] = queue_rcv.popleft()
                pg_pos += 1
                print(pg_pos)
            except IndexError:
                print('queue_rcv empty!')
                pg_pos += 1
                return register, pg_pos, queue_snd, queue_rcv, count_snd

pg_pos_a = 0
pg_pos_b = 0

queue_a = deque([])
queue_b = deque([])

register_a = {'p' : 0}
register_b = {'p' : 1}

count_a = 0
count_b = 0

while True:
    register_a, pg_pos_a, queue_b, queue_a, count_a = run(pg_pos_a, register_a, queue_b, queue_a, count_a)
    register_b, pg_pos_b, queue_a, queue_b, count_b = run(pg_pos_b, register_b, queue_a, queue_b, count_b)
    if queue_a.__len__() == 0 and queue_b.__len__() == 0:
        break
    
print(count_a)
