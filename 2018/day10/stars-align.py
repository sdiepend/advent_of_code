import re
from time import sleep

with open("input.txt") as f:
    content = f.readlines()

points_pos = []
points_vel = []
for line in content:
    pos_x, pos_y, vel_x, vel_y = re.match(r'^position=<([ -]?[0-9]+), ([ -]?[0-9]+)> velocity=<([ -]?[0-9]+), ([ -]?[0-9]+)>', line.strip()).groups()
    points_pos.append([int(pos_x), int(pos_y)])
    points_vel.append([int(vel_x), int(vel_y)])

margin = 5
print(points_pos)
print(points_vel)
seconds = 0
while True:
    
    min_x = min(map(lambda x: x[0], points_pos))
    max_x = max(map(lambda x: x[0], points_pos))
    min_y = min(map(lambda x: x[1], points_pos))
    # print(min_y)
    max_y = max(map(lambda x: x[1], points_pos))
    # print(max_y)
    
   

    if max_y - min_y < 20 and max_y - min_y > 8:
        grid = [['.' for x in range((max_x - min_x) + margin)] for x in range((max_y - min_y) + margin)]
    
        for point in points_pos:
            grid[point[1]-min_y][point[0]-min_x] ='#'
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
        print(seconds)
        print('------------------------------------------------------------------')
        
    new_points_pos = []
    for i in range(len(points_vel)):
        new_points_pos.append([points_pos[i][0] + points_vel[i][0], points_pos[i][1] + points_vel[i][1]])
    # print(new_points_pos)
    
    points_pos = new_points_pos
    seconds += 1