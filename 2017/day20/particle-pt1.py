import re
with open('input') as f:
    content = f.readlines()

content = [x.strip().split() for x in content]
particles = []
for line in content:
    particle = []
    for el in line:
        x = int(re.sub(r'[pva]=<([-0-9]+),.*', r'\1', el))
        y = int(re.sub(r'[pva]=<([-0-9]+),([-0-9]+),.*', r'\2', el))
        z = int(re.sub(r'[pva]=<([-0-9]+),([-0-9]+),([-0-9]+)>.*', r'\3', el))
        values = [x,y,z]
        particle.append(values)
    particles.append(particle)
# use re.match and groups

def tick(particles):
    for particle in particles:
        # for in range(3)      
        i = 0
        while i < 3:
            particle[1][i] += particle[2][i]
            i += 1
        i = 0
        while i < 3:
            # move statement up
            particle[0][i] += particle[1][i]
            i += 1
#        print(particle)
    return particles

def calc_min_sum(particles):
    sums = []
    for particle in particles:
        sum = 0
        for x in particle[0]:
            sum = sum + abs(x)
        sums.append(sum)
    return sums.index(min(sums))

i = 0
while i < 1000:
    particles = tick(particles)
    print(calc_min_sum(particles))
    i += 1
