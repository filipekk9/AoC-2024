import re

def mul(x,y):
    return x*y

sum = 0
add = True
input = open("input.txt", "r").read()

pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

good = re.findall(pattern, input)

for x in good:
    if x == "do()":
        add = True
    elif x == "don't()":
        add = False
    elif add:
            sum += eval(x)

print(sum)
