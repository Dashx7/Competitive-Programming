numLines = int(input())

mydict = dict()
for i in range(numLines):
    name = input()
    first,last, course = name.split()
    full = ""+first+last
    if (course in mydict):
        mydict[course].add(full)
    else:
        mydict[course] = set()
        mydict[course].add(full)
    # print(mydict)

outputlist = []
for key, value in mydict.items():
    outputlist.append([key,len(value)])
    # print(key, len(value))
outputlist.sort()
# print (outputlist)
for item in outputlist:
    print (item[0], item[1])
    