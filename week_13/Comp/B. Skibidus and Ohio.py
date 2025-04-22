n = int(input())
for i in range(n):
    word = input()
    sum = 1
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            sum = 1
            break
        else:
            sum += 1
    print(sum)
