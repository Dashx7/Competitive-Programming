n,m = map(int,input().split())

cansizes = []
for _ in range(n):
    cansize = int(input())
    cansizes.append(cansize)

cansizes.sort()
total_waste = 0

# sizes = [0]*m
# largest_size = 0
for i in range(m):
    size_needed = int(input())
    temp = 0 # Linear search
    for j in range(n):
        if cansizes[j] >= size_needed:
            waste = cansizes[j] - size_needed
            total_waste += waste
            break
        
print(total_waste)
    

    

