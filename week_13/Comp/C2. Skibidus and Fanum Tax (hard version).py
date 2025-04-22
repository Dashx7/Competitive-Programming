tests = int(input())
from collections import defaultdict
for _ in range(tests):
    n, m = map(int, input().split()) # Sizes of a and b
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    bSet = set(b) # Set of b for O(1) lookup

    dp = defaultdict(set) # Maps from last a[i] to the used set of b
    nextDp = defaultdict(set) # for the next update
    dp[a[0]] = set() #
    for j in range(len(b)):
        newVal = b[j] - a[0]
        dp[newVal].add(b[j])
    
    for i in range(1,len(a)):
        for key, usedSet in dp.items():
            if a[i] >= key:
                nextDp[a[i]] = usedSet # No change case if its still non decreasing

            for j in range(len(b)):
                if b[j] not in usedSet: # We could still use it (not in the used set)
                    newVal = b[j] - a[i]
                    if newVal >= key: # Non decreasing
                        nextDp[newVal] = dp[key] | {b[j]}
        
        dp = nextDp.copy() # Copy the next table to the current table
        nextDp = defaultdict(set) # Reset the next table for the next hall
    if len(dp) == 0:
        print("NO")
    else:
        print("YES")



