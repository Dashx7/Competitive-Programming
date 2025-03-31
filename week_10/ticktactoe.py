turn = input()

def test(grid):
    # Check 3 in a row
    ops = [(0,1),(1,0),(1,1),(1,-1)]
    for op in ops:
        for i in range(3):
            if grid[3*i] == grid[3*i+1] == grid[3*i+2] == turn:
                return turn
            if grid[i] == grid[i+3] == grid[i+6] == turn:
                return turn
            if grid[0] == grid[4] == grid[8] == turn:
                return turn
            if grid[2] == grid[4] == grid[6] == turn:
                return turn
    return "?" if '.' in grid else "-"

while True:
    grid = input() + input() + input()

    print(grid)
    break