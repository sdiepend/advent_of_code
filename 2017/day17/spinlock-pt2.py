circ_list = []
step_size = 349
i = 0
pos = 0
while i < 50000000:
    circ_list.insert(pos,i)
    pos = (pos + step_size + 1) % len(circ_list)
    i += 1

print(circ_list[circ_list.index(0) + 1])
