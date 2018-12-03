with open("input") as f:
    content = f.readlines()

claims = [x.strip().split(' ') for x in content]

fabric = [ [0 for x in range(1000)] for x in range(1000)]

for claim in claims:
    start_x = int(claim[2].split(',')[0])
    start_y = int(claim[2].split(',')[1].strip(':'))
    width = int(claim[3].split('x')[0])
    height = int(claim[3].split('x')[1])
    for i in range(start_y, start_y + height):
        for j in range(start_x, start_x + width):
            fabric[i][j] += 1

overlap_count = 0
for row in range(1000):
    for col in range(1000):
        if fabric[row][col] >= 2:
            overlap_count += 1

print(overlap_count)