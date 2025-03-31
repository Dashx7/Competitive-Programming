from collections import defaultdict

numNodes = int(input())
nodesToConnections = defaultdict(int)
adjList = defaultdict(lambda: [0] * numNodes)

def query(Nodes):
    print("?", *Nodes, flush=True)
    val = int(input())
    nodesToConnections[tuple(Nodes)] = val

for i in range(1,numNodes+1):
    query([i]) # Query them on their own

for i in range(1,numNodes+1):
    for j in range(i+1,numNodes+1):
        query([i,j]) # Query them together
        if nodesToConnections[i] + nodesToConnections[j] != nodesToConnections[tuple([i,j])]:
            adjList[i-1][j-1] = 1
            adjList[j-1][i-1] = 1
        if sum(adjList[i-1]) == nodesToConnections[tuple([i])]:
            break

print("!", flush=True)
for i in range(numNodes):
    print(*adjList[i], flush=True)

            
    