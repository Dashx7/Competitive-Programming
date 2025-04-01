from collections import defaultdict
t : int = int(input())

def isValidColoring(adjGraph, city, color, colorMap):
    for neighborCity in adjGraph[city]:
        if neighborCity in colorMap and colorMap[neighborCity] == color:
            return False
    return True

def graphColoringUtil(adjGraph, numColors, colorMap, cities, index):
    if index == len(cities):
        return True # All cities have been colored
    
    city = cities[index] # Getting next city
    for color in range(1, numColors + 1): # Index by 1 because default dict sets to 0
        if isValidColoring(adjGraph, city, color, colorMap):
            colorMap[city] = color
            if graphColoringUtil(adjGraph, numColors, colorMap, cities, index + 1): # Recurse
                return True
            del colorMap[city]  # Backtrack
    
    return False
def solveMapColoring(adjGraph):
    for i in range(1, 5):
        colorMap = defaultdict(int)
        cities = list(adjGraph.keys()) # Only need to actually try the cities with connections
        if graphColoringUtil(adjGraph, i, colorMap, cities, 0):
            # print("Works at:", i)
            print(i)
            return
    print("many")
    return

for _ in range(t):
    c, b = map(int, input().split())

    adjGraph = defaultdict(list)
    for _ in range(b):
        c1, c2 = map(int, input().split())
        adjGraph[c1].append(c2)
        adjGraph[c2].append(c1)
    
    solveMapColoring(adjGraph) # solve the map coloring problem and print the number of colors needed




