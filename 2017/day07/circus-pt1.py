import re

with open("input") as f:
    content = f.readlines()

towers = {}
for line in content:
    new_line = line.split()
    tower = [re.sub(',','',x) for x in new_line]
    if '->' in tower:
        towers[tower[0]] = tower[tower.index('->')+1:]
    else:
        towers[tower[0]] = 'leaf'

def find_root(node):
    parent = None
    for key, value in towers.items():
        if node in value:
            parent = key
    if parent is not None:
        find_root(parent)
    else:
        print(node)
        
find_root('apcztdj')
