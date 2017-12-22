import re

with open('input') as f:
    content = f.readlines()

tube_grid = []

for line in content:
    grid_line = [x.strip() for x in line]
    tube_grid.append(grid_line)

moves = {'down': (1,0),
         'up': (-1,0),
         'left': (0,-1),
         'right': (0,1),
         'stop': (0,0) }

dir = 'down'
letters = ''
i = 0 
j = tube_grid[0].index('|')

while dir != 'stop':
    move_i, move_j = moves[dir]
    next_i, next_j = i + move_i, j + move_j
    if tube_grid[next_i][next_j] == '+':
        if tube_grid[next_i][next_j-1] == '-' and next_i != i and next_j-1 != j:
            dir = 'left'
        elif tube_grid[next_i][next_j+1] == '-' and next_i != i and next_j+1 != j:
            dir = 'right'
        elif tube_grid[next_i-1][next_j] == '|' and next_i-1 != i and next_j != j:
            dir = 'up'
        elif tube_grid[next_i+1][next_j] == '|' and next_i+1 != i and next_j != i:
            dir = 'down'
    elif tube_grid[next_i][next_j] == '':
        dir = 'stop'
    elif re.match('[A-Z]', tube_grid[next_i][next_j]):
        letters = letters + tube_grid[next_i][next_j]

    i = next_i
    j = next_j

print(letters)

