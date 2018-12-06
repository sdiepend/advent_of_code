from collections import Counter, defaultdict
with open("input.txt") as f:
    content = f.readlines()

coordinates = [[int(x.split(', ')[0]), int(x.split(', ')[1].strip())] for x in content]

coords = sorted(coordinates, key=lambda k: [k[0], k[1]])

min_x = coords[0][0]
print(min_x)
min_y = sorted(coordinates, key=lambda k: k[1])[0][1]
print(min_y)
max_x = coords[-1][0]
print(max_x)
max_y = sorted(coordinates, key=lambda k: k[1])[-1][1]
print(max_y)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

bound = 100
def calculate_counts(bound):
    counts = defaultdict(lambda: 0)
    grid = [['.' for x in range(min_x-bound, max_x+bound)] for y in range(min_y-bound, max_y+bound) ]
    for row in range(min_y-bound, max_y+bound):
        for col in range(min_x-bound, max_x+bound):
            distances = {}
            for i in range(len(coords)):
                distances[i] = manhattan_distance([col, row], coords[i])
            closest_val = min(distances.values())
            # print(distances)
            # print(closest_val)
            closest_coord = [k for k, v in distances.items() if v == closest_val]
            # print(closest_coord)
            
            if len(closest_coord) == 1:
                grid[(row-min_y)-bound][(col-min_x)-bound] = closest_coord[0]
                counts[closest_coord[0]] += 1
    return counts

counts1 = calculate_counts(10)
counts2 = calculate_counts(20)

finite_counts = []
for k, v in counts1.items():
    if counts2[k] == v:
        finite_counts.append(v)

print(max(finite_counts))