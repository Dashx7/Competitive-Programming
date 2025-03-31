import math
from collections import defaultdict 
prime = []
def SieveOfEratosthenes(num):
    global prime
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
             for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

testcases = int(input())
tests = [None] * testcases
maxRange = -1
for g in range(testcases):
    a, b, p = map(int, input().split())
    maxRange = max(maxRange, b-a)
    tests[g] = [a,b,p]
# print("MaxRange: ", maxRange)
SieveOfEratosthenes(maxRange+1)
# print(prime)

defaultDict = defaultdict(int) # Default to 0
for i in range(testcases):
    a, b, p = tests[i]
    for k in range(p, maxRange+1):
        primeV = -1
        # print("k: ", k)
        if prime[k] == True:
            primeV = k
        else:
            continue
        # print("Is valid")

        secondNum = a/primeV
        secondNum = int(math.ceil(secondNum))
        firstNum = secondNum * primeV
        secondNum+=1
        secondNum*=primeV
        for j in range(secondNum, b+1, primeV):
            # print(j)
            # if defaultDict[j] != 0:

            defaultDict[defaultDict[j]] = firstNum # Set the default value to the first number
            defaultDict[j] = firstNum
        else:
            continue
    setCount = 0
    for j in range(a, b+1):
        # print("j: " + str(j) + " " + str(defaultDict[j]))
        if defaultDict[j] == 0 or defaultDict[j] == j: # If not found or is the first number in the set
            setCount+=1
    print("Case #" + str(i+1) + ": " + str(setCount))
