# Find my family
k = int(input())
left_right = []

list_of_potential_canidates = []

def find_lowest_left_and_insert(height):
    leftpointer = 0; rightpointer = len(left_right) - 1
    while leftpointer <= rightpointer:
        mid = (leftpointer + rightpointer) // 2
        if left_right[mid] < height:
            leftpointer = mid + 1
        else:
            rightpointer = mid - 1
    # Value of leftpointer is the index where the height should be inserted
    left_right.insert(leftpointer, height)
    next_larger_height = left_right[leftpointer+1] if leftpointer+1 < len(left_right) else None
    return next_larger_height
for i in range(k):
    left_right = []
    lowest_left_num = None

    n = int(input())
    heights = list(map(int, input().split()))

    for height in heights:
        if not left_right:
            left_right.append(height)
            continue
        elif lowest_left_num != None and height > lowest_left_num:
            list_of_potential_canidates.append(i+1)
            break
        else:
            lowest_left_num = find_lowest_left_and_insert(height)

print(len(list_of_potential_canidates))
print(*list_of_potential_canidates, sep="\n")