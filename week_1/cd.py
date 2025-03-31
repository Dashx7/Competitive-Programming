first, second = map(int, input().split())

while(first and second):
    setAll = set()
    for _ in range(first):
        input_value = int(input())
        setAll.add(input_value)
        
    dups = 0
    for _ in range(second):
        input_value = int(input())
        if input_value in setAll:
            dups+=1
    print(dups)
    first, second = map(int, input().split())
