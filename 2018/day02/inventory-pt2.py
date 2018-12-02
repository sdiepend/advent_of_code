with open("input") as f:
    content = f.readlines()

ids = [x.strip() for x in content]

for id in ids:
    for id2 in ids:
        diff = 0
        new_id = []
        for i in range(len(id)):
            if id[i] != id2[i]:
                diff += 1
            else:
                new_id.append(id[i])
        if diff == 1:
            print(''.join(new_id))