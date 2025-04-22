numDice = 8
wormDieValues = [1, 2, 3, 4, 5, 6] # where # 6 is still worth 5

n = int(input())

for _ in range(n):
    score = int(input())

# Looks hard to calculate the combinations but IDK how DP fixes this yet