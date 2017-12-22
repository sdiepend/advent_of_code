import math
num = 325489

lower = math.floor(math.sqrt(num))
upper = math.ceil(math.sqrt(num))
print(lower)
print(upper)
lowest = int(math.pow(lower,2))
upest = int(math.pow(upper,2))
print(lowest)
print(upest)
corner = math.ceil((upest + lowest) / 2)
print(corner)
if ((upper % 2) == 0):
    steps = upper
    print(steps)
else:
    steps = upper - 1


if corner - steps < num < corner:
    final_steps = steps - (corner - num)
elif corner < num :
    final_steps = steps - (num - corner)
else:
    final_steps = steps

print(final_steps)
