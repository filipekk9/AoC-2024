input = [list(map(int,x.split(" "))) for x in open("input2.txt", "r").read().splitlines()]
safe = 0

for x in input:
    is_safe = 0
    asc = all(y < z for y,z in zip(x, x[1:]))
    dsc = all (y > z for y,z in zip(x, x[1:]))

    if asc:
        asc3 = all(y > z - 4 for y,z in zip(x,x[1:]))
        if asc3:
            safe +=1
            is_safe +=1

    if dsc:
        dsc3 = all(y < z + 4 for y, z in zip(x, x[1:]))
        if dsc3:
            safe+=1
            is_safe +=1

    if is_safe == 0:
        list_safe = 0
        for i in range(len(x)):
            list = x[:i] + x[i+1:]
            list_asc = all(y < z for y, z in zip(list, list[1:]))
            list_dsc = all(y > z for y, z in zip(list, list[1:]))

            if list_asc:
                list_asc3 = all(y > z - 4 for y,z in zip(list,list[1:]))
                if list_asc3:
                    list_safe +=1
            elif list_dsc:
                list_dsc3 = all(y < z + 4 for y, z in zip(list, list[1:]))
                if list_dsc3:
                    list_safe +=1
        if list_safe > 0:
            safe+=1


print (safe)