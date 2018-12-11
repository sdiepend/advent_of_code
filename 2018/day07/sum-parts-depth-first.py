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



start_nodes = []

for key, value in children.items():
    found = False
    for value in children.values():
        if key in value:
            found = True
    if not found:
        start_nodes.append(key)
    children[key] = sorted(children[key])

children['ST'] = sorted(start_nodes)
start_node = 'ST'
for node in start_nodes:
    parents[node].append(start_node)

end_node = ''

for key in parents.keys(): 
    end_found = False
    for value in parents.values():
        if key in value:
            end_found = True
    if end_found is False:
        end_node = key

for key in parents.keys():
    parents[key] = sorted(parents[key])

print(start_node)
print(end_node)
ordered = OrderedDict()

print(children)
print(parents)

node = start_node

while node != end_node:
    # print(node)
    if len(children[node]) != 0:
        next = children[node][0]
        if len(parents[next]) == 1:
            ordered[next] = node
            children[node].pop(children[node].index(next))
            parents[next].pop(parents[next].index(node))
            node = next
        elif len(parents[next]) > 1:
            parents[next].pop(parents[next].index(node))
            children[node].pop(children[node].index(next))
    else:
        # print("lengte is 0")
        next = ordered[node]
        # parents[node].pop(parents[node].index(next))
        node = next
    print(parents[node])
    print(ordered)

print(parents[node])
print(''.join(ordered.keys()))