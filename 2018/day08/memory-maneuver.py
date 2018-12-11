with open("input_example.txt") as f:
    content = f.readline().split(' ')

print(content)
def get_metadata(content):
    if content[0] == 0:
        return content[-content[1]]
    else:
        return content

