# circ_list = [0, 1, 2, 3, 4]
# lengths = [3, 4, 1, 5]

circ_list = list(range(256))
input = '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118'
lengths = [ ord(x) for x in input] + [17, 31, 73, 47, 23]
print(lengths)

def knot_hash(circ_list, start_pos, skip_size):
    i = 0
    while i < len(lengths):
        end_pos = start_pos + lengths[i]
        if end_pos < len(circ_list):
            circ_list = list(circ_list[:start_pos] + circ_list[start_pos:end_pos][::-1] + circ_list[end_pos:])
        else:
            end_pos = end_pos % len(circ_list)
            temp_list = circ_list[start_pos:] + circ_list[:end_pos]
            temp_list = temp_list[::-1]
            circ_list = temp_list[len(temp_list)-end_pos:] + circ_list[end_pos:start_pos] + temp_list[:len(temp_list)-end_pos]
        start_pos = start_pos + lengths[i] + skip_size
        if start_pos >= len(circ_list):
            start_pos = start_pos % len(circ_list)
        skip_size += 1
        i += 1
    return circ_list, start_pos, skip_size

def dense_hash(to_hash):
    


start_pos = 0
skip_size = 0
i = 0
while i < 64:
    circ_list, start_pos, skip_size = knot_hash(circ_list, start_pos, skip_size)
    print(start_pos)
    i += 1
