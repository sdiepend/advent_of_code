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

total = 0        
i = 0
while i < 40000000:
    value_a = (value_a * factor_a) % divider
    bin_a = "{0:b}".format(value_a)
    value_b = (value_b * factor_b) % divider
    bin_b = "{0:b}".format(value_b)
    if match(bin_a, bin_b):
        total += 1
    i += 1

print(total)
