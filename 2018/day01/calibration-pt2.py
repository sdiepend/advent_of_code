with open("input") as f:
    content = f.readlines()

frequencies = [x.strip() for x in content]

i = 0
final_freq = 0
inter_freqs = []

while True:
    final_freq += int(frequencies[i % len(frequencies)])
    if final_freq in inter_freqs:
        print(final_freq)
        break
    else:
        inter_freqs.append(final_freq)
        i += 1