#stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

with open('input') as f:
    stream = f.readline()

i = 0
ignore = False
level = 0
points = 0
removed = 0

while i < len(stream):
    if ignore:
        if stream[i] == "!":
            i += 2
        elif stream[i] == ">":
            ignore = False
            i += 1
        else:
            i += 1
            removed += 1
    else:
        if stream[i] == "{":
            level += 1
        if stream[i] == "}" and level != 0:
            points = points + level
            level -= 1
        if stream[i] == "<":
            ignore = True
        i += 1

print(points)
print(removed)
