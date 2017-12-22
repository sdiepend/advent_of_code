import re
from collections import Counter
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

def tick(particles):
    for particle in particles:
#        print(particle)
        i = 0
        while i < 3:
            particle[1][i] += particle[2][i]
            i += 1
        i = 0
        while i < 3:
            particle[0][i] += particle[1][i]
            i += 1
#        print(particle)
    return particles

def remove_collision(particles):
    new_list = list(particles)
    i = 0
    while i < len(particles):
        j = 0
        while j < len(particles):
            if particles[i][0] == particles[j][0] and i != j: 
                if particles[i] in new_list:
                    new_list.remove(particles[i])
            j += 1
        i += 1
    return new_list              

i = 0
while i < 100:
    particles = tick(particles)
    particles = remove_collision(particles)
    print(len(particles))
    i += 1
# write stop condition -> stop when closest pos is same als lowest acc
