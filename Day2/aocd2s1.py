def if_asc(x):
    result = all(y < z for y,z in zip(x, x[1:]))
    return result

def is_safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(diff in range(1, 4) for diff in diffs) or all(diff in range(-3, 0) for diff in diffs)

def if_dsc(x):
    result = all (y > z for y,z in zip(x, x[1:]))
    return result

def if_asc_morethan3(x):
    result = all(y > z - 4 for y,z in zip(x,x[1:]))
    return result

def if_dsc_morethan3(x):
    result = all(y < z + 4 for y, z in zip(x, x[1:]))
    return result

input = [list(map(int,x.split(" "))) for x in open("input2.txt", "r").read().splitlines()]
safe = 0
res = [is_safe(l) for l in input].count(True)
print(res)
for x in input:

    asc = if_asc(x)
    dsc = if_dsc(x)

    if asc:
        asc3 = if_asc_morethan3(x)
        if asc3:
            safe +=1

    if dsc:
        dsc3 = if_dsc_morethan3(x)
        if dsc3:
            safe+=1

print(safe)







