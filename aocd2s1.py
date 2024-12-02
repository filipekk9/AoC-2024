input = [list(map(int,x.split(" "))) for x in open("input2.txt", "r").read().splitlines()]
safe = 0
for x in input:

    asc = all(y < z for y,z in zip(x, x[1:]))
    dsc = all (y > z for y,z in zip(x, x[1:]))

    if asc:
        asc3 = all(y > z - 4 for y,z in zip(x,x[1:]))
        if asc3:
            safe +=1

    if dsc:
        dsc3 = all(y < z + 4 for y, z in zip(x, x[1:]))
        if dsc3:
            safe+=1

print(safe)







