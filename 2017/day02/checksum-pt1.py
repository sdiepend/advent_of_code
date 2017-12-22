with open("input") as f:
    numbers = [list(map(int,x.strip().split('\t'))) for x in f.readlines()]

sum = 0

for line in numbers:
    sum = sum + max(line) - min(line)

print(sum)
