#        hashSum += ord(subtring[i]) * (31 ** i)

inputString = input()

hashes = {}
for i, char in enumerate(inputString):
    
    hashed = ord(char)