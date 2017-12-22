import re

with open("input") as f:
    content = f.readlines()

class Tower():
    def __init__(self, name='root', weight=0, children=None):
        self.name = name
        self.weight = int(weight)
        self.children = []
    def __repr__(self):
        print_node = ''
        for child in self.children:
            print_node += child.name
        return print_node
    def add_child(self, node):
        assert isinstance(node, Tower)
        self.children.append(node)

towers = {}
for line in content:
    new_line = line.split()
    tower = [re.sub(r'\(([0-9]*)\)',r'\1',re.sub(',','',x)) for x in new_line]
    if tower[0] not in towers: 
        towers[tower[0]] = Tower(tower[0], weight=tower[1])
    else:
        towers[tower[0]].weight = int(tower[1])
    if '->' in tower:
        for sub_tower in tower[tower.index('->') + 1:]:
            if sub_tower in towers:
                towers[tower[0]].add_child(towers[sub_tower])
            else:
                towers[sub_tower] = Tower(sub_tower)
                towers[tower[0]].add_child(towers[sub_tower])

def calc_weight(tower):
    total_weight = tower.weight
    if tower.children:
        for sub_tower in tower.children:
            total_weight = total_weight + calc_weight(sub_tower)
        return total_weight
    else:
        return total_weight

for tower in towers.values():
    if tower.children:
        child_weights = []
        for sub_tower in tower.children: 
            child_weights.append(calc_weight(sub_tower))
        if len(set(sorted(child_weights))) > 1:
            print(tower.name + ' ' + str(tower.weight) + ' ' + str(child_weights))
            for sub_tower in tower.children:
                print(sub_tower.weight)
