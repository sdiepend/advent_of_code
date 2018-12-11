with open("input.txt") as f:
    polymer = f.readline().strip()

def react(polymer_list):
    i = 0
    while i < (len(polymer_list)-1):
        if polymer_list[i].islower() and polymer_list[i].upper() == polymer_list[i + 1]:
            # print(polymer_list[i] + " " + polymer_list[i + 1])
            polymer_list.pop(i)
            polymer_list.pop(i)
        elif polymer_list[i].isupper() and polymer_list[i].lower() == polymer_list[i + 1]:
            # print(polymer_list[i] + " " + polymer_list[i + 1])
            polymer_list.pop(i)
            polymer_list.pop(i)
        elif i != 0 and polymer_list[i].islower() and polymer_list[i].upper() == polymer_list[i - 1]:
            polymer_list.pop(i)
            polymer_list.pop(i-1)
        elif i != 0 and polymer_list[i].isupper() and polymer_list[i].lower() == polymer_list[i - 1]:
            polymer_list.pop(i)
            polymer_list.pop(i-1)
        else:
            i += 1
    return polymer_list

part1_list = list(polymer)

# Part 1
for x in range(500):
    part1_list = react(part1_list)

print(len(part1_list))

# Part 2
polymer_lengths = []
for letter in "abcdefghijklmnopqrstuvwxyz":
    part2_list = list(polymer.replace(letter, "").replace(letter.upper(), ""))
    for x in range(2000):
        part2_list = react(part2_list)
    polymer_lengths.append(len(part2_list))
print(min(polymer_lengths))