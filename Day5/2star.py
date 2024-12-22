import math
input = [line.strip() for line in open("input.txt", "r")]

criteria = []
updates = []
dcriteria = {}
sum = 0

for line in input:
    if "|" in line:
        criteria.append(line.strip())
    elif "," in line:
        updates.append(line.strip())

for criterion in criteria:
    key = criterion[:2]
    value = criterion[3:]

    if key in dcriteria:
        dcriteria[key].append(value)
    else:
        dcriteria[key] = [value]

for update in updates:
    dic = {}
    up = update.split(",")
    for i in up:
        try:
            dic[i] = set(up) & set(dcriteria[i])
            dic[i] = len(dic[i])
        except KeyError:
            dic[i] = 0
            pass
    order = sorted(dic, key=dic.get, reverse=True)
    if order != up:
        mid = math.floor(len(order)/2)
        sum += int(order[mid])

print(sum)
