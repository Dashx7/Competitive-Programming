def findChain(n,m, chains):
    if n ==0 or m == 0:
        pass
    else:
        bigger = max(n,m)
        smaller = min(n,m)
        i = 0
        while bigger >= smaller:
            i += 1
            bigger = bigger - smaller
        chains.append((bigger, smaller, i))
        findChain(bigger, smaller, chains)


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    chains = []
    findChain(n, m, chains)
    # print("Chain: ", chains)

    lastChainWin = None
    for chain in chains[::-1]:
        if chain[2] > 1:
            lastChainWin = 1
        elif chain[0] ==0 or chain[1] == 0:
            lastChainWin = 1
        else:
            lastChainWin = lastChainWin ^ 1 # XOR to say its the loss if win and win if loss
    if lastChainWin:
        print("Stan wins")
    else:
        print("Ollie wins")

# 34 12
# 15 24
# 0 0
