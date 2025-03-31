# import random
# from collections import defaultdict

# numNodes = int(input())

# adjList = defaultdict(set)

# # Making a random graph for simulation
# for i in range(1,numNodes+1):
#     for j in range(1,numNodes+1):
#         if i != j:
#             if random.randint(0,1):
#                 adjList[i].add(j)
#                 adjList[j].add(i)
# print(adjList)

# class group: # A group of node connections
#     def __init__(self):
#         self.connections = set()
#         self.minConnections = -1
#         self.maxConnections = -1
# def queryCutSolve(nodes):
    
# def queryCutSim(nodes):
#     numCuts = 0
#     for node in nodes:
#         for neighbor in adjList[node]:
#             if neighbor not in nodes:
#                 numCuts += 1
#     queryCutSolve(nodes)
#     return numCuts

# connectionToIndex = {}    
# index = 0
# for i in range(1,numNodes+1):
#     for j in range(1,numNodes+1):
#         if i != j:
#             connectionToIndex[(i,j)] = index
#             connectionToIndex[(j,i)] = index
#             index += 1

# while True:
#     inputNodes = list(map(int, input().split()))
#     print(f"Query Cut is {queryCutSim(inputNodes)}", flush=True)