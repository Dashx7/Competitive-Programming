n = int(input())

sqrt_n = int(n**0.5) # Rounded down
sqrt_n += 1

while sqrt_n > 0:
    if 2*n % sqrt_n == 0:
        print(n)
        break
    else:
        sqrt_n += 1
