n = int(input())

from functools import lru_cache
@lru_cache(maxsize=2**20)
def findMin(gameInt : int):
    #Slid masks
    leftMask = [0b110, 0b001]
    rightMask = [0b011, 0b100]
    selector = 0b111
    bestScore = bin(gameInt).count('1')
    for i in range(2,23):
        # Check if left mask
        # print("Left Mask:", bin(leftMask[0]), "Right Mask:", bin(rightMask[0]))
        # print("Selector:", bin(selector))
        # print("GameInt:", bin(gameInt))
        # print()
        if selector & gameInt == leftMask[0]:
            newGameInt = (gameInt & ~selector) | leftMask[1]
            bestScore = min(bestScore, findMin(newGameInt))
        # Check if right mask
        if selector & gameInt == rightMask[0]:
            newGameInt = (gameInt & ~selector) | rightMask[1]
            bestScore = min(bestScore, findMin(newGameInt))
        # Update masks, shifting one over
        leftMask[0] = leftMask[0] << 1; leftMask[1] = leftMask[1] << 1
        rightMask[0] = rightMask[0] << 1; rightMask[1] = rightMask[1] << 1
        selector = selector << 1
    return bestScore

for _ in range(n):
    gameState = map(str, input())
    # print("Game state:", gameState)
    gameInt = 0
    for char in gameState:
        gameInt = (gameInt << 1) + (1 if char == 'o' else 0) 
    # print(gameInt)
    # print(bin(gameInt))
    print(findMin(gameInt)) # Actual answer

#---oo----------oo------
