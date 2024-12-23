lines = [line.strip() for line in open("input.txt", "r")]
sum = 0
d = 0
curr_pos = None
pos = [[-1,0],[0,1],[1,0],[0,-1]]
i =0
for line in lines:
    if line.find("^") != -1:
        curr_pos = [i,line.find("^")]
    i+=1
lines = [list(line) for line in lines]


while True:
        try:
            is_move = False
            for _ in range(len(pos)):
                move = [curr_pos[0] + pos[d][0], curr_pos[1] + pos[d][1]]
                if curr_pos[0] < 0 or curr_pos[1] <0:
                    break
                lines[curr_pos[0]][curr_pos[1]] = "X"
                if lines[move[0]][move[1]] == "." or lines[move[0]][move[1]] == "X":
                    curr_pos = move
                    is_move = True
                    break
                elif lines[move[0]][move[1]] == "#":
                    d = (d + 1) % 4
            if not is_move:
                break
        except IndexError:
            break
for line in lines:
    sum += line.count("X")
print(sum)
