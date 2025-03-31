def extended_gcd(a, b):
    if a ==0:
        return b, 0, 1 #
    gcd, x1, y1 = extended_gcd(b%a, a)
    x = y1 - (b//a) * x1 # Going up the chain of substitutions
    y = x1
    return gcd, x, y

def mod_inverse(Y, N): # Calculated the modular inverse of Y mod N using the extended euclidean algorithm
    gcd, x, y = extended_gcd(Y, N)
    if gcd != 1:
        return None
    else:
        return x % N

def modular_division(X, Y, N):
    Y_inverse = mod_inverse(Y, N)
    if Y_inverse == None:
        return -1
    else:
        return (X * Y_inverse) % N


while(True):
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    for _ in range(t):
        x, operation, y = input().split()
        x, y = int(x), int(y)
    
        if operation == "+":
            print( (x + y) % n )
        elif operation == "-":
            print( (x - y) % n )
        elif operation == "*":
            print((x%n * y%n) % n)
        elif operation == "/":
            # X * Y^-1 mod N
            print(modular_division(x, y, n))


