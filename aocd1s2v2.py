input = [x.split("   ") for x in open("input1.txt", "r").read().splitlines()]
left = [int(x[0]) for x in input]
right = [int(x[1]) for x in input]

for i in range(1_000):
    occurrences = {}

    for x in right:
        if x not in occurrences:
            occurrences[x] = 1
        else:
            occurrences[x] += 1

    sum = 0
    for x in left:
        if x in occurrences:
            sum += x * occurrences[x]
# print(sum)
