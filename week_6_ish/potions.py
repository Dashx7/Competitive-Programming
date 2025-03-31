
green, red = map(int, input().split())

minVal = min(green,red)
health = 10* minVal
green -=minVal; red -=minVal

if green %3 == 1:
    health+= 1
elif green %3 == 2:
    health+=3
health+= green//3 * 10

print(health)
