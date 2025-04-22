while(True):
    n = int(input())
    if n == 0:
        break

    from collections import defaultdict
    adjGraph = defaultdict(list)
    parentGraph = defaultdict(lambda:-1)
    values = defaultdict(int)
    for i in range(1,n+1):
        allnumbers = list(map(int, input().split()))
        n = allnumbers[0]
        m = allnumbers[1]
        values[i] = m
        d = allnumbers[2]
        a = allnumbers[3:]
        for item in a:
            adjGraph[i].append(item)
            parentGraph[item] = i

    # print("Printing adjGraph")
    # for key, value in adjGraph.items():
    #     print(f"{key}: {value}") 
    # print("Printing parentGraph")
    # for key, value in parentGraph.items():
    #     print(f"{key}: {value}")
    def bfs(start, adjGraph):
        visited = set() # prevent traveling up the tree
        depthLevels = []
        queue = [start]
        while queue:
            visited.update(queue)
            queue = [child for parent in queue for child in adjGraph[parent] if child not in visited]
            # visited.add(child for child in queue)
            if queue:
                depthLevels.append(queue)
            # print("Depth levels:", depthLevels)
        return depthLevels

    depthLevels = bfs(1, adjGraph)
    # print(depthLevels)


    #Backwards traversal of levels
    totalChanges = 0
    for level in depthLevels[::-1]:
        for node in level:
            nodeChange = 1-values[node] # If 0, it needs 1
            totalChanges += abs(nodeChange)
            values[parentGraph[node]] -= nodeChange # It then removes the change from its parent
            
    # print("Total changes:", totalChanges)
    print(totalChanges)
