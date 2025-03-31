# Manachester's algo
import sys

def findAllSubstrings(word):
    processedWord = "".join([("#" + char) if char != "\n" else "" for char in word])
    processedWord = processedWord + "#"
    # print(processedWord)
    
    left = 0
    right = 0
    center = 0
    p = [0] * len(processedWord)

    allPalindromes = set()
    for i in range(len(processedWord)):
        mirror = 2*center - i
        if i < right:
            p[i] = min(right-i,p[mirror])
        a = i + (1 + p[i])
        b = i - (1 + p[i])
        while a < len(processedWord) and b >= 0 and processedWord[a] == processedWord[b]:
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
        if p[i] > 1:
            allPalindromes.add("".join([char for char in processedWord[i-p[i]:i+p[i]+1] if char != "#"]))
    # print(p)

    newPalindromes = set()
    for palinrome in allPalindromes: # Turn each palindrome into a smaller palindrome
        while len(palinrome) > 3:
            palinrome = palinrome[1:-1]
            if palinrome not in newPalindromes:
                newPalindromes.add(palinrome)
            else:
                break
    allPalindromes = allPalindromes.union(newPalindromes) # Union
    listedPalindromes = list(allPalindromes)
    listedPalindromes.sort()
    print(*listedPalindromes)
        
        

for word in sys.stdin:
    findAllSubstrings(word)
    print()
    