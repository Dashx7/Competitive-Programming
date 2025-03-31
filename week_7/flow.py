grid = []
for i in range(4):
    grid.append(list(input().strip()))

# print(grid)

solvableGrids = [grid]
def connectColor(grid,x,y,color):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    if grid[x][y] != "W" and grid[x][y] != "WW" and grid[x][y] != color:
        print("grid[x][y]",x,y,grid[x][y])
        print("color",color)   
        return False # If not white, or the first square, stop it
    if x > 0 and grid[x-1][y] == color or x < 3 and grid[x+1][y] == color or y > 0 and grid[x][y-1] == color or y < 3 and grid[x][y+1] == color:
        solvableGrids.append(grid)
    else:
        if x > 0 and (grid[x-1][y] == "W"): #Left is empty
            grid[x-1][y] = "WW" # Use WW to connect so the check doesn't see its own tail
            if connectColor(grid,x-1,y,color):
                solvableGrids.append(grid)
            grid[x-1][y] = "W"
        if x < 3 and (grid[x+1][y] == "W"): #Right
            grid[x+1][y] = "WW"
            if connectColor(grid,x+1,y,color):
                solvableGrids.append(grid)
            grid[x+1][y] = "W"  
        if y > 0 and (grid[x][y-1] == "W"): #Up
            grid[x][y-1] = "WW"
            if connectColor(grid,x,y-1,color):
                solvableGrids.append(grid)
            grid[x][y-1] = "W"
        if y < 3 and (grid[x][y+1] == "W"): #Down
            grid[x][y+1] = "WW"
            if connectColor(grid,x,y+1,color):
                solvableGrids.append(grid)
            grid[x][y+1] = "W"
    return  

for color in ["R","G","B","Y"]:
    shouldBreak = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] == color:
                newGrids = [connectColor(pgrid,i,j,color) for pgrid in solvableGrids]
                print("newGrids",newGrids)
                shouldBreak = True; break
        if shouldBreak: break

if len(solvableGrids) == 0:
    print("not solvable")
else:
    print("solvable")