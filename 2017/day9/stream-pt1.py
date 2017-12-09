#stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

with open('input') as f:
    stream = f.readline()


i = 0
ignore = False
level = 0
points = 0

while i < len(stream):
    if ignore:
        if stream[i] == ">":
            j = i - 1
            count = 0
            while stream[j] == "!":
                count += 1
                j -= 1
            if count % 2 == 1:
                ignore = True
            else:
                ignore = False
        i += 1
    else:
        if stream[i] == "{":
            print("{")
            level += 1
        if stream[i] == "}" and level != 0:
            print("}")
            points = points + level
            level -= 1
        if stream[i] == "<":
            ignore = True
        i += 1

print(points)



