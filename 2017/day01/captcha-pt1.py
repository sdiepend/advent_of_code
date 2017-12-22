input = '1113'
sum = 0

for i in range(input.__len__()):
    if i == input.__len__()-1:
        if input[i] == input[0]:
            sum = sum + int(input[i])
    else:
        if input[i] == input[i+1]:
            sum = sum + int(input[i])

print(sum)
