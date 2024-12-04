import re

def get_diagonals_lr(grid, len):
    diagonals = []
    for diag in range(2 * len - 1):
        diagonal = []
        for row in range(len):
            ind = diag - row
            if 0 <= ind < len:
                diagonal.append(grid[row][ind])
        diagonals.append("".join(diagonal))
    return diagonals

def get_diagonals_rl(grid, len):
    diagonals = []
    for diag in range(2 * len - 1):
        diagonal = []
        for row in range(len):
            ind = row - diag + len - 1
            if 0 <= ind < len:
                diagonal.append(grid[row][ind])
        diagonals.append("".join(diagonal))
    return diagonals


def xmas_finder(grid):
    count = 0
    for row in grid:
        results = re.findall(pattern, row)
        results_r = re.findall(pattern_r, row)
        count += len(results)
        count += len(results_r)
    return count



input_horizontal = [line.strip() for line in open("input.txt", "r")]
input_vertical = list(zip(*input_horizontal))
input_vertical = ["".join(letter) for letter in input_vertical]
count = 0
pattern = r"XMAS"
pattern_r = r"SAMX"

count += (xmas_finder(input_vertical) + xmas_finder(input_horizontal) + xmas_finder(get_diagonals_lr(input_horizontal, len(input_horizontal))) + xmas_finder(get_diagonals_rl(input_horizontal, len(input_horizontal))))

print(count)

