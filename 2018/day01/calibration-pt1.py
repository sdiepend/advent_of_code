with open("input") as f:
    content = f.readlines()

frequencies = [x.strip() for x in content]

final_freq = 0

for freq in frequencies:
    final_freq += int(freq)

print(final_freq)