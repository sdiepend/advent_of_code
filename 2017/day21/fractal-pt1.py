import numpy as np
from pprint import pprint

with open('input') as f:
    content = f.readlines()

transforms = [x.strip().split(' => ') for x in content]

rules = []
for rule in transforms:
    rule_new = []
    for pattern in rule:
        pattern_new = pattern.split('/')
        chars = [list(x) for x in pattern_new]
        rule_new.append(chars)
    rules.append(rule_new)


def find_rule(A):
    for rule in rules:
        B = np.array(rule[0])
        if np.array_equal(A, B):
            return np.array(rule[1])

def transform(grid):
    A = np.array(grid)
    # rotate the array zero times, one time, two times, three times
    for i in range(4):
        A_rot = np.rot90(A, k=i, axes=(1,0))
        new_grid = find_rule(A_rot)
        if new_grid is not None:
            return new_grid
        
        # flip the array for every rotation
        for j in range(2):
            A_rot_flip = np.flip(A_rot, j)
            new_grid = find_rule(A_rot_flip)
            if new_grid is not None:
                return new_grid
            j += 1
        i += 1

def iterate(grid):
    print(len(grid))
    if len(grid) == 3:
        final_grid = transform(grid)
        print(final_grid)
    elif len(grid) % 3 == 0 and len(grid) != 3:
        parts = int(len(grid)/3)
        print(parts)
        final_grid = np.array([['.' for _ in range((parts * 3) + parts)]])
        print(final_grid)
        for i in range(parts):
            row_grid = np.array([[] for _ in range(4)])
            for j in range(parts):
                sub_grid = grid[i*3:(i*3)+3, j*3:(j*3)+3]
                print(sub_grid)
                sub_grid = transform(sub_grid)
                row_grid = np.concatenate((row_grid, sub_grid), axis=1)
            final_grid = np.concatenate((final_grid, row_grid), axis=0)
        final_grid = final_grid[1:,:]
        print(final_grid)
    elif len(grid) % 2 == 0:
        parts = int(len(grid)/2)
        print(parts)
        final_grid = np.array([['.' for _ in range((parts * 2) + parts)]])
        for i in range(parts):
            row_grid = np.array([[] for _ in range(3)])
            for j in range(parts):
                sub_grid = grid[i*2:(i*2)+2, j*2:(j*2)+2]
                sub_grid = transform(sub_grid)
                row_grid = np.concatenate((row_grid, sub_grid), axis=1)
            final_grid = np.concatenate((final_grid, row_grid), axis=0)
        final_grid = final_grid[1:,:]
    return final_grid

grid = np.array([['.', '#', '.'], 
                 ['.', '.', '#'], 
                 ['#', '#', '#']])


for _ in range(5):
    grid = iterate(grid)
    
count = 0
for row in grid:
    for el in row:
        if el == '#':
            count += 1



print(grid)
print(count)
