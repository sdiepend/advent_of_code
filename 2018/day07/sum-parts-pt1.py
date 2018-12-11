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

ordered = []
available = []

for key, value in children.items():
    found = False
    for value in children.values():
        if key in value:
            found = True
    if not found:
        available.append(key)

while len(available) > 0:
    node = sorted(available)[0]
    ordered.append(node)
    for child in children[node]:
        parents[child].pop(parents[child].index(node))
        if len(parents[child]) == 0:
            available.append(child)
    available.pop(available.index(node))

print(''.join(ordered))


# for node in start_nodes:
#     parents[node].append(start_node)

# end_node = ''

# for key in parents.keys(): 
#     end_found = False
#     for value in parents.values():
#         if key in value:
#             end_found = True
#     if end_found is False:
#         end_node = key

# for key in parents.keys():
#     parents[key] = sorted(parents[key])

# print(start_node)
# print(end_node)
# ordered = OrderedDict()

# print(children)
# print(parents)

# node = start_node

# while node != end_node:
#     # print(node)
#     if len(children[node]) != 0:
#         next = children[node][0]
#         if len(parents[next]) == 1:
#             ordered[next] = node
#             children[node].pop(children[node].index(next))
#             parents[next].pop(parents[next].index(node))
#             node = next
#         elif len(parents[next]) > 1:
#             parents[next].pop(parents[next].index(node))
#             children[node].pop(children[node].index(next))
#     else:
#         # print("lengte is 0")
#         next = ordered[node]
#         # parents[node].pop(parents[node].index(next))
#         node = next
#     print(parents[node])
#     print(ordered)

# print(parents[node])
# print(''.join(ordered.keys()))