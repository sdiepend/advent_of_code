factor_a = 16807
factor_b = 48271

divider = 2147483647

value_a = 277
value_b = 349

# value_a = 65
# value_b = 8921

def match(bin_a, bin_b):
    if bin_a[-16:] == bin_b[-16:]:
         return True

def find_next_a(value):
    value = (value * factor_a) % divider
    if (value % 4) == 0:
        return(value)
    else:
        return(find_next_a(value))

def find_next_b(value):
    value = (value * factor_b) % divider
    if (value % 8) == 0:
        return value
    else:
        return (find_next_b(value))

total = 0       
pairs = 0
while pairs < 5000000:
    value_a = find_next_a(value_a)
    bin_a = "{0:b}".format(value_a)
    value_b = find_next_b(value_b)
    bin_b = "{0:b}".format(value_b)
    if match(bin_a, bin_b):
        total += 1
    pairs += 1

print(total)
