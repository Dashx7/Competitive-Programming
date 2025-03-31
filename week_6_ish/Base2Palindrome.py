M = int(input())

def turnBinaryToBase10(binary):
    # print("Binary: ", binary)
    # print()
    base10 = 0
    for i in range(len(binary)):
        base10 += int(binary[i]) * (2 ** (len(binary) - i - 1)) # Actually had it backqards but it worked bc palindromic properties
    # print("Base 10: ", base10)
    print(base10)
    return base10

def findBinaryPalindromes(M):
    # print("Finding binary palindromes for M = ", M)
    odds = ["1"]
    evens = ["11"]
    if M == 0:
        turnBinaryToBase10("0") # Not an actual case but just in case
        return
    elif M == 1:
        turnBinaryToBase10("1")
        return
    elif M == 2:
        turnBinaryToBase10("11")
        return
    oddsNext = True
    previous_lengths = 0
    while True:
        middle = len(evens[0]) // 2 # 11 -> 1 -> substring [0,1]
        if oddsNext:
            previous_lengths += len(odds)
            odds = [evens[0][:middle] + "0" + evens[0][middle:], evens[0][:middle] + "1" + evens[0][middle:]]
            # print("New odds: ", odds)
            if len(odds) + len(evens) + previous_lengths >= M:
                turnBinaryToBase10(odds[M - len(evens) - 1 - previous_lengths])
                return
            
        elif not oddsNext:
            previous_lengths += len(evens)
            evens = [evens[0][:middle] + "00" + evens[0][middle:], evens[0][:middle] + "11" + evens[0][middle:]]
            # print("New evens: ", evens)

            if len(odds) + len(evens) + previous_lengths >= M:
                turnBinaryToBase10(evens[M - len(odds) - 1 - previous_lengths])
                return
        oddsNext = not oddsNext
    return

findBinaryPalindromes(M)
    
