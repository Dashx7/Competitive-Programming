stringS = input()

queries = int(input())

for _ in range(queries):
    l, r = map(int, input().split())
    subtring = stringS[l:r]
    hashSum = 0
    for i in range(len(subtring)):
        hashSum += ord(subtring[i]) * (31 ** i)
    print(hashSum)