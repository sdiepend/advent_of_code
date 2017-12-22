import math
from decimal import *

with open("input") as f:
    content = f.readline()

numbers = [int(x) for x in content.strip().split('\t')]

# numbers = [0,2,7,0]

states = []
count = 0

while True:
    count = count + 1
    size = len(numbers)
    max_value = max(numbers)
    max_index = numbers.index(max(numbers))
    i = (max_index + 1) % len(numbers)
    while size != 0:
        numbers[max_index] = 0
        to_add = math.ceil(max_value/size)
        max_value = max_value - to_add
        size = size - 1
        numbers[i] = numbers[i] + to_add
        i = (i + 1) % len(numbers)
    
    if numbers in states:
        cycle_size = len(states) - states.index(numbers)
        break
    else:
        states.append(list(numbers))
    
print(count)
print(cycle_size)
