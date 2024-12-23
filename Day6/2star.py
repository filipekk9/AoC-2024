def input():
    data = [line.strip() for line in open("input.txt", "r")]
    data = [list(line) for line in data]
    return data
def start_position():
    lines = [line.strip() for line in open("input.txt", "r")]
    i =0
    for line in lines:
        if line.find("^") != -1:
            return [i, line.find("^")]
        i += 1
def possible_obstruction_positions():
    curr = start_position()
    lines = input()
    pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    d =0
    obstruction = []
    while True:
            try:
                is_move = False
                for _ in range(len(pos)):
                    move = [curr[0] + pos[d][0], curr[1] + pos[d][1]]
                    if curr[0] < 0 or curr[1] <0:
                        break
                    lines[curr[0]][curr[1]] = "X"
                    if lines[move[0]][move[1]] == "." or lines[move[0]][move[1]] == "X":
                        if lines[move[0]][move[1]] == ".":
                            obstruction.append(move)
                        curr = move
                        is_move = True
                        break
                    elif lines[move[0]][move[1]] == "#":
                        d = (d + 1) % 4
                if not is_move:
                    break
            except IndexError:
                break
    return obstruction
def is_loop(x):
    curr = start_position()
    lines = x
    times = {}
    pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    d = 0
    while True:
            try:
                is_move = False
                for _ in range(len(pos)):
                    move = [curr[0] + pos[d][0], curr[1] + pos[d][1]]
                    if move[0] < 0 or move[1] < 0:
                        break
                    if lines[move[0]][move[1]] == "." or lines[move[0]][move[1]] == "^":
                        if f"{move[0]},{move[1]}" in times:
                            times[f"{move[0]},{move[1]}"] += 1
                        else:
                            times[f"{move[0]},{move[1]}"] = 1
                        if times[f"{move[0]},{move[1]}"] > 4:
                            return True
                        curr = move
                        is_move = True
                        break
                    elif lines[move[0]][move[1]] == "#":
                        d = (d + 1) % 4

                if not is_move:
                    break
            except IndexError:
                break

    return False


def main():
    obstruction = possible_obstruction_positions()
    sum = 0
    for obs in obstruction:
        lines = input()
        lines [obs[0]][obs[1]] = "#"
        if is_loop(lines):
            sum+=1
    print(sum)

if __name__ == "__main__":
    main()
