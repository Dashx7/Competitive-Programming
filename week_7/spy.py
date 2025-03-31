from collections import defaultdict

numTest = int(input())

for i in range(numTest):
    numLines = int(input())
    m = defaultdict(list) # Trying with default dict so no need for checking invalid keys
    for j in range(numLines):
        slist = input().split(" ")
        m[slist[1]].append(slist[0])

    product = 1
    for k, v in m.items():
        product *= len(v) + 1
    print(product - 1)