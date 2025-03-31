N, K = map(int,input().split())

nList = list(map(int, input().split()))
kList = list(map(int, input().split()))

listOfKnown = set(nList)
listOfKnown.add(0)
newAngles = set(nList)

kSet = set(kList)

while newAngles:
    curAngle = newAngles.pop()

    addedNew = False
    toADD = set()
    for otherAngle in listOfKnown:
        generatedAngle = curAngle + otherAngle
        generatedAngle %= 360
        if generatedAngle in listOfKnown:
            pass
        else:
            addedNew = True
            toADD.add(generatedAngle)
        
        if curAngle < otherAngle:
            generatedAngle = curAngle - otherAngle
            generatedAngle %= 360
            if generatedAngle in listOfKnown:
                pass
            else:
                addedNew = True
                toADD.add(generatedAngle)
    listOfKnown.update(toADD) #Maybe
    if (addedNew):
        newAngles.add(curAngle)


for k in kList:
    if k in listOfKnown:
        print("YES")
    else:
        print("NO")



