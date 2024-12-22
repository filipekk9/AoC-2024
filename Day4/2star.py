import re

def get_grids_3x3(grid, grid_len):
    subgrids = []

    for row_start in range(grid_len - 2):
        for col_start in range(grid_len - 2):
            subgrid = [row[col_start:col_start + 3] for row in grid[row_start:row_start + 3]]
            subgrids.append(subgrid)
    return subgrids

input = [line.strip() for line in open("input.txt", "r")]
count = 0
grids_3x3 = get_grids_3x3(input, len(input))

for grid in grids_3x3:
    if re.match(r".A.", grid[1]):
        if (re.match(r"M.M", grid[0]) and re.match(r"S.S", grid[2])) or \
            (re.match(r"S.S", grid[0]) and re.match(r"M.M", grid[2])) or \
            (re.match(r"S.M", grid[0]) and re.match(r"S.M", grid[2])) or \
            (re.match(r"M.S", grid[0]) and re.match(r"M.S", grid[2])):
            count+=1

print(count)

