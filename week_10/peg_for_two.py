# 3
# 1 6
# 1 7 8
# 5 0 3 4
# 9 3 2 1 9

vals = []
for i in range(5):
    vals.append(list(map(int, input().split())))

def action(a,b,c): # Score, new abc
    if a == 0 and b != 0 and c != 0:
        return (b*c, c, 0, 0)
    elif a != 0 and b !=0 and c == 0:
        return (a*b, 0, 0, a)
    return (0, 0, 0, 0)

from copy import deepcopy
from functools import lru_cache

def is_game_over(vals):
    for i in range(3):
        for j in range(3):
            if j > i:
                continue
            if action(vals[i][j], vals[i+1][j], vals[i+2][j]) != (0, 0, 0, 0):
                return False
            if action(vals[i][j], vals[i+1][j+1], vals[i+2][j+2]) != (0, 0, 0, 0):
                return False
            if action(vals[i+2][j], vals[i+2][j+1], vals[i+2][j+2]) != (0, 0, 0, 0):
                return False

class gameState:
    def __init__(self, vals):
        self.vals = deepcopy(vals)
        self.p1Advantage = 0
        self.turn = -1
    
    def evaluateWinner(self):
        if is_game_over(self.vals):
            return self.turn
        else:
            return None
    
    def play(self):
        self.turn = -self.turn
        winner = self.evaluateWinner()
        if winner is not None:
            return self.p1Advantage
        bestAdv = None
        for i in range(3):
            for j in range(3):
                if j > i:
                    continue
                act = action(vals[i][j], vals[i+1][j], vals[i+2][j]) != (0, 0, 0, 0):
                    newGame = gameState(vals)
                    newGame.p1Advantage = self.p1Advantage + act[0]*self.turn
                    newGame.vals[i][j] = act[1]
                    newGame.vals[i+1][j] = act[2]
                    newGame.vals[i+2][j] = act[3]
                    new

                if action(vals[i][j], vals[i+1][j+1], vals[i+2][j+2]) != (0, 0, 0, 0):
                    return False
                if action(vals[i+2][j], vals[i+2][j+1], vals[i+2][j+2]) != (0, 0, 0, 0):
                    return False
                

            


print(vals)