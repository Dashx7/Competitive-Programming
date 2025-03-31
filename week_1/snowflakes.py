#SLIDING WINDOW NOW
tests = int(input())
for _ in range(tests):
    n = int(input())
    snowflakes = []
    for _ in range(n):
        snowflakes.append(int(input()))
    
    seen = set()
    leftindex = 0
    max_length = 0
    
    for rightindex in range(n):
        while snowflakes[rightindex] in seen:
            seen.remove(snowflakes[leftindex])
            leftindex += 1 #slide right
        seen.add(snowflakes[rightindex])
        max_length = max(max_length, rightindex - leftindex + 1)
    print(max_length)
            
