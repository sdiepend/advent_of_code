with open("input") as f:
    content = f.readlines()

claims = [x.strip().split(' ') for x in content]

fabric = [ [[] for x in range(1000)] for x in range(1000)]

for claim in claims:
    start_x = int(claim[2].split(',')[0])
    start_y = int(claim[2].split(',')[1].strip(':'))
    width = int(claim[3].split('x')[0])
    height = int(claim[3].split('x')[1])
    for i in range(start_y, start_y + height):
        for j in range(start_x, start_x + width):
            fabric[i][j].append(claim[0])

for claim in claims:
    start_x = int(claim[2].split(',')[0])
    start_y = int(claim[2].split(',')[1].strip(':'))
    width = int(claim[3].split('x')[0])
    height = int(claim[3].split('x')[1])
    only_one = True
    for i in range(start_y, start_y + height):
        for j in range(start_x, start_x + width):
            if len(fabric[i][j]) != 1:
                only_one = False
    if only_one == True:
        print(claim[0])