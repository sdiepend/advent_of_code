with open("input") as f:
    content = f.readlines()

phrases = [x.strip().split(' ') for x in content]

count = 0

for phrase in phrases:
    phrase = [''.join(sorted(word)) for word in phrase]

    if len(phrase) == len(set(phrase)):
        count += 1

print(count)
