import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Keeps track of "heads"
        self.rank = [1] * n  # avoids tall trees. End Mii
        
    def find(self, x): # Gets parent (head) of set containing x.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): #Keeps it organized.
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def prime_factors(x, primes):
    factors = set()
    for p in primes:
        if x % p == 0:
            factors.add(p)
            while x % p == 0:
                x //= p
    if x > 1:
        factors.add(x)
    return factors

t = int(input()) 
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

max_b = -1
for test in test_cases:
    max_b = max(max_b, test[1] - test[0])

primes = sieve_of_eratosthenes(max_b)

for case_num, (a, b, k) in enumerate(test_cases, start=1):
    uf = UnionFind(b - a + 1)
    
    for i in range(a, b + 1):
        factors = prime_factors(i, primes)
        for factor in factors:
            if factor >= k:
                for j in range(i + factor, b + 1, factor):
                    uf.union(i - a, j - a)
    
    leader_count = len(set(uf.find(i - a) for i in range(a, b + 1)))
    
    print(f"Case #{case_num}: {leader_count}")