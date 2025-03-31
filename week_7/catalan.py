import math

tests = int(input())

for _ in range(tests):
    n = int(input())
    print(math.comb(2 * n, n) // (n + 1)) # Catalan number formula
