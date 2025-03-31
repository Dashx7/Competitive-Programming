# Understand this code if you dare
n, m = map(int, input().split())

def closest(a):
    # print("Running closest with a:", a)
    sum = 0
    iterations = 0
    while sum < a:
        iterations += 1
        sum += iterations
    
    if sum == a:
        return iterations, 0
    return iterations, a - (sum - iterations)

def sumOfIncrementing(a):
    return (a * (a + 1)) // 2

left_over = m - n + 1 # removing out the first n-1 connections from city 1 to n
iterations, mod = closest(left_over)

# print(iterations, mod)
num_isolated = None
if iterations == 0:
    num_isolated = n - 1 # -1 because node -> edges is 1 less than nodes
else:
    num_isolated = n - iterations - 2
# print("num_isolated:", num_isolated)
isolatede_sum = sumOfIncrementing(m) - sumOfIncrementing(m - num_isolated)
# print(isolatede_sum)

runup = 0; incrementor = 0; x = 1; Full = 1 if mod >0 else 0
while x < n - num_isolated - Full:
    runup += incrementor
    incrementor += x
    x += 1
if x != 1:
    runup+=x-1
# print("runup:", runup)

inbetween = 0
if mod != 0:
    inbetween = m-num_isolated - (mod)
# print("inbetween:", inbetween)
total = isolatede_sum + runup + inbetween
# print("total:", total)
print(total)