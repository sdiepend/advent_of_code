with open("input") as f:
    content = f.readlines()

phrases = [x.strip().split(' ') for x in content]

count = 0

for phrase in phrases:
    if len(phrase) == len(set(phrase)):
        count += 1

print(count)
