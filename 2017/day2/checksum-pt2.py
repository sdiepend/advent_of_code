with open("input") as f:
    content = f.readlines()

numbers = [x.strip().split('\t') for x in content]

sum = 0

for line in numbers:
    for x in line:
        for y in line:
            if x is not y:
                if int(x) % int(y) == 0:
                    sum = sum + (int(x)/int(y))

print(sum)
