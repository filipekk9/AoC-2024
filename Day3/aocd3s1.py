import re

def mul(x,y):
    return x*y

sum = 0
input = open("input.txt", "r").read()

pattern = r"mul\(\d+,\d+\)"

good = re.findall(pattern, input)

print(good)

for x in good:
    sum += eval(x)

print(sum)