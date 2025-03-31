print(1, flush=True)
alt = 1
while True:
    response = int(input().strip())
    if response == 99:
        break # Lost
    if response == 97 or response == 98:
        print(99, flush=True)
        break # Won
    elif response %3 == 1:
        response += 2
    elif response %3 == 2:
        response += 1 # Keep on %3 == 0
    else:
        response += 1+ alt # Give alternating answers
        alt ^= 1
    print(response, flush=True)
