input = [x.split("   ") for x in open("input1.txt", "r").read().splitlines()]
left = [int(x[0]) for x in input]
right = [int(x[1]) for x in input]
for i in range(1_000):
    sum = 0

    for x in left:
        sum+= x * right.count(x)


# print(sum)

