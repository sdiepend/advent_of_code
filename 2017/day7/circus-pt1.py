from anytree import Node, RenderTree, LevelOrderIter

with open("test-input") as f:
    content = f.readlines()

towers = [x.strip().strip().split(' ') for x in content]
print(towers)

nodes = []
i = 0
while i < len(towers):
    node = Node(towers[i][0])
    nodes.append(node)
    if '->' in towers[i]:
        j = towers[i].index('->') + 1
        while j < len(towers):
            child_node = Node(towers[i][j], parent=node)
            j += 1
            nodes.append(child_node)
    print(RenderTree(node))     
    i += 1
