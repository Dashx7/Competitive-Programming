# Precompute ranges
ranges = []  # List of tuples (start, end, step)
start = 1
step = 1
while True:
    if step == 1:
        end = 1
    elif step == 2:
        end = 9
    else:
        end = 10**(10**(step - 2)) - 1
    
    ranges.append((start, end, step))
    
    # Break if range exceeds practical limits (10^6 digits)
    if end > 10**6:
        break
    
    start = end + 1
    step += 1

# Function to determine the stabilization step
def find_steps(n):
    for start, end, step in ranges:
        if start <= n <= end:
            return step
    return -1  # Failsafe, should never occur

# Input processing
inp = input()
while inp != "END":
    n = int(inp)
    print(find_steps(n))
    inp = input()
