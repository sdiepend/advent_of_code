from collections import Counter, defaultdict
with open("input_cha.txt") as f:
    content = f.readlines()

coordinates = [[int(x.split(', ')[0]), int(x.split(', ')[1].strip())] for x in content]

coords = sorted(coordinates, key=lambda k: [k[0], k[1]])

min_x = coords[0][0]
min_y = sorted(coordinates, key=lambda k: k[1])[0][1]
max_x = coords[-1][0]
max_y = sorted(coordinates, key=lambda k: k[1])[-1][1]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calculate_counts(bound):
    region = 0
    counts = defaultdict(lambda: 0)
    grid = [['.' for x in range(min_x-bound, max_x+bound)] for y in range(min_y-bound, max_y+bound) ]
    for row in range(min_y-bound, max_y+bound):
        for col in range(min_x-bound, max_x+bound):
            distances = {}
            for i in range(len(coords)):
                distances[i] = manhattan_distance([col, row], coords[i])
            if sum(distances.values()) < 10000:
                region += 1
            closest_val = min(distances.values())

            closest_coord = [k for k, v in distances.items() if v == closest_val]
            
            if len(closest_coord) == 1:
                grid[(row-min_y)-bound][(col-min_x)-bound] = closest_coord[0]
                counts[closest_coord[0]] += 1
    return counts, region

counts1, _ = calculate_counts(0)
counts2, region = calculate_counts(1)

finite_counts = []
for k, v in counts1.items():
    if counts2[k] == v:
        finite_counts.append(v)

print("Largest Finite Area(pt1): {area}, Region(pt2): {region}".format(area=max(finite_counts), region=region))