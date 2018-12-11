import re, time
from collections import defaultdict, OrderedDict
with open("input.txt") as f:
    content = f.readlines()

children = defaultdict(lambda: [])
parents = defaultdict(lambda: [])
for line in content:
    first, second = re.match(r'^Step (\S) .* step (\S) .*', line.strip()).groups()
    children[first].append(second)
    parents[second].append(first)

workers = ['.' for x in range(5)]
in_process = defaultdict(lambda: 0)
available = []
ordered = []

for key, value in children.items():
    found = False
    for value in children.values():
        if key in value:
            found = True
    if not found:
        available.append(key)

second = 0
while True: 
    for i in range(5):
        if workers[i] == '.' and len(available) > 0:
            node = sorted(available)[0]
            workers[i] = node
            in_process[node] = (ord(node) - 64) + 60
            available.pop(available.index(node))
    print(workers)

    for k, value in in_process.items():
        value -= 1
        if value == 1:
            ordered.append(k)
            for child in children[k]:
                parents[child].pop(parents[child].index(k))
                if len(parents[child]) == 0:
                    available.append(child)
            workers[workers.index(k)] = '.'
        in_process[k] = value
    for k, v in list(in_process.items()):
        if v == 0:
            del in_process[k]
    print(in_process)
    if len(available) == 0 and len(in_process) == 0:
        break
    second += 1

print(second)
print(''.join(ordered))