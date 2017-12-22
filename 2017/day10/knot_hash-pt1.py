# circ_list = [0, 1, 2, 3, 4]
# lengths = [3, 4, 1, 5]

circ_list = list(range(256))
print(circ_list)
lengths = [106, 118, 236, 1, 130, 0, 235, 254, 59, 205, 2, 87, 129, 25, 255, 118]

skip_size = 0
i = 0
start_pos = 0
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
result = circ_list[0] * circ_list[1]
print(result)
