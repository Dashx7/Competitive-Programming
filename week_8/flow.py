from copy import deepcopy
flowBoard = []
for _ in range(4):
    flowBoard.append(list(input().strip()))

# print(flowBoard)

def connectedCheck(board, x, y, color):
    if board[x][y] == color:
        return True
    return False

potentialBoards = [flowBoard]
def connectColor(board, x, y, color):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    if connectedCheck(board, x, y, color):
        potentialBoards.append(deepcopy(board)) # Add a COPY of the board
        return True
    if board[x][y] != "W": # If not currently on an empty square that wasn't the color you were looking for, stop it. get some help
        return False
    else:
        board[x][y] = "WW" # Indicates its being used
        connectColor(board, x-1, y, color)
        connectColor(board, x+1, y, color)
        connectColor(board, x, y-1, color)
        connectColor(board, x, y+1, color)
        board[x][y] = "W"

colors = ['R','G','B','Y']
for color in colors:
    toBreak = False
    for i in range(4):
        for j in range(4):
            if flowBoard[i][j] == color:
                runningBoards = potentialBoards
                potentialBoards = []
                for runningBoard in runningBoards:
                    runningBoard[i][j] = "W"
                    connectColor(runningBoard,i,j,color)
                toBreak = True
                break
        if toBreak:
            break
for potentialBoard in potentialBoards:
    # print(potentialBoard)
    # print()
    white = 'W'
    exists = any(white in sublist for sublist in potentialBoard)
    if not exists: # Has no white squares
        print("solvable")
        exit()
print("not solvable")
            