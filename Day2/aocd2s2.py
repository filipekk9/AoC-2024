input = [list(map(int,x.split(" "))) for x in open("input2.txt", "r").read().splitlines()]
safe = 0

def if_asc(x):
    result = all(y < z for y,z in zip(x, x[1:]))
    return result

def if_dsc(x):
    result = all (y > z for y,z in zip(x, x[1:]))
    return result

def if_asc_morethan3(x):
    result = all(y > z - 4 for y,z in zip(x,x[1:]))
    return result

def if_dsc_morethan3(x):
    result = all(y < z + 4 for y, z in zip(x, x[1:]))
    return result

for x in input:
    is_safe = 0
    asc = if_asc(x)
    dsc = if_dsc(x)

    if asc:
        asc3 = if_asc_morethan3(x)
        if asc3:
            safe +=1
            is_safe +=1

    if dsc:
        dsc3 = if_dsc_morethan3(x)
        if dsc3:
            safe+=1
            is_safe +=1

    if is_safe == 0:
        list_safe = 0
        for i in range(len(x)):
            list = x[:i] + x[i+1:]
            list_asc = if_asc(list)
            list_dsc = if_dsc(list)

            if list_asc:
                list_asc3 = if_asc_morethan3(list)
                if list_asc3:
                    list_safe +=1
            elif list_dsc:
                list_dsc3 = if_dsc_morethan3(list)
                if list_dsc3:
                    list_safe +=1
        if list_safe > 0:
            safe+=1

print (safe)