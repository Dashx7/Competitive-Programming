def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(Y, N):
    gcd, x, y = extended_gcd(Y, N)
    if gcd != 1:
        return None # Shouldn't happen
    else:
        return x % N
    
t = int(input())
for _ in range(t):
    a, n, b, m = map(int, input().split())

    k = n * m
    part1 = m % k * mod_inverse(m, n) %k * a % k # Get the mod inverse for +1, then *a for +a
    part2 = n % k * mod_inverse(n, m) %k * b % k # Get the mod inverse for +1, then *b for +b
    print((part1 + part2) % k, k)