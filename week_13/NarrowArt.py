n, k = map(int, input().split())

halls = []
for _ in range(n):
    left, right = map(int, input().split())
    halls.append((left, right))
finishingVal = map(int, input().split()) # Useless

transition = dict()
transition[tuple([0, 0])] = [tuple([0, 0]), tuple([0, 1]), tuple([1, 0])]
transition[tuple([0, 1])] = [tuple([0, 0]), tuple([0, 1])]
transition[tuple([1, 0])] = [tuple([0, 0]), tuple([1, 0])]

#Bitmask DP
from collections import defaultdict
dpTable = defaultdict() # maskleft, maskright, blockedrooms -> min blockedVal
dpTable[tuple([0,0,0])] = 0 # No blocked rooms and no score
nextTable = defaultdict(int)  
for hall in halls:
    # print("Hall:", hall)
    for key, value in dpTable.items():
        # print("Key:", key, "Value:", value)
        mask = tuple(key[0:2])
        for transitionMask in transition[mask]: # Potiential new masks
            # print("Portential Transition mask:", transitionMask)
            unblockedVal = value
            unblockedVal+= hall[0] if not transitionMask[0] else 0
            unblockedVal+= hall[1] if not transitionMask[1] else 0
            roomsBlocked = key[2] + (transitionMask[0] or transitionMask[1])
            nextTable[tuple(transitionMask + (roomsBlocked,))] = max(nextTable[tuple(transitionMask + (roomsBlocked,))], unblockedVal) # Set the new value to min between the old and the new    dpTable = nextTable
    dpTable = nextTable.copy() # Copy the next table to the current table
    nextTable = defaultdict(int) # Reset the next table for the next hall

# print(dpTable)
# print(dpTable[tuple([0,0,k])])
# print(dpTable[tuple([0,1,k])])
# print(dpTable[tuple([1,0,k])])
print(max(dpTable[tuple([0,0,k])], dpTable[tuple([0,1,k])], dpTable[tuple([1,0,k])]))