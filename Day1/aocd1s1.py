input = [x.split("   ") for x in open("input1.txt", "r").read().splitlines()]
left = [int(x[0]) for x in input]
right = [int(x[1]) for x in input]
left = sorted(left)
right = sorted(right)
res = sum([abs(x - y) for x, y in zip(left, right)])
print(res)
