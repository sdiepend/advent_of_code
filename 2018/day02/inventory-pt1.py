with open("input") as f:
    content = f.readlines()

ids = [x.strip() for x in content]

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

occurances = {}

for id in ids:
    letter_counts = {key : val for key, val in alphabet.items() }
    for letter in id:
        letter_counts[letter] += 1
    
    for val in set(letter_counts.values()):
        if val in occurances and val > 1:
            occurances[val] += 1
        elif val > 1:
            occurances[val] = 1

print(occurances)
checksum = 1

for num in occurances.values():
    checksum = checksum * num

print(checksum)