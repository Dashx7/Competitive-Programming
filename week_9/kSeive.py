n, k = map(int, input().split())

def SieveOfEratosthenes(num, k):
    primes = [True for i in range(n+1)]
    count = 0
    p = 2

    while(p<=num):
        if (primes[p] == True):
            count += 1
            if count == k:
                print(p)
                return
            for i in range(p*p, num+1, p):
                if primes[i] == True:
                    primes[i] = False
                    count += 1
                    # print(str(i) + "now marked, count: " + str(count))
                    if count == k:
                        print(i)
                        return
        p += 1
    print("Not found :(")

SieveOfEratosthenes(n, k)