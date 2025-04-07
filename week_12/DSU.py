from collections import defaultdict

class DSU: # Disjoint Set Union (Union-Find) class curtesy of chat
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [1] * n  # Rank is used to keep the tree balanced

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:  # Only merge if they are in different sets
            if self.rank[rootX] > self.rank[rootY]:  
                self.parent[rootY] = rootX  # Attach Y under X
            elif self.rank[rootX] < self.rank[rootY]:  
                self.parent[rootX] = rootY  # Attach X under Y
            else:  
                self.parent[rootY] = rootX  
                self.rank[rootX] += 1  # Increase rank when merging equal ranks
    def count_scc(self):
        unique_roots = set(self.find(i) for i in range(len(self.parent)))
        return len(unique_roots) -1 # -1 to account for the root itself

m, n = map(int, input().split())

def BFS(start, end, adjacency_list):
    queue = [(start, [start])]  # Queue stores tuples of (current_node, path_to_current_node)
    visited = set()
    visited.add(start)
    
    while queue:
        node, path = queue.pop(0)  
        if node == end:
            return path  # Return the path if the end node is reached
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  # Append the neighbor and its path
    return [] # Shouldn't trigger

adjacency_list = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
# Sort the adjacency list for consistent ordering
for key in adjacency_list:
    adjacency_list[key].sort()
onEdges = set()
for _ in range(n):
    u, v = map(int, input().split())
    dsu = DSU(m + 1)  # Create a DSU

    path = BFS(u, v, adjacency_list)
    if path:
        # print("Path found:", path)  # Print the path
        for i in range(len(path) - 1):
            tupledEdge = tuple(sorted([path[i], path[i + 1]]))
            if tupledEdge not in onEdges:
                onEdges.add(tupledEdge)
            else:
                # print("Edge already exists, removing it from DSU" + str(tupledEdge))
                onEdges.remove(tupledEdge) # Hit a second time so remove
        for edge in onEdges:
            dsu.union(edge[0], edge[1])
    else:
        print("No path found") # Shouldn't trigger
        continue
    # Print the number of unique components
    print(dsu.count_scc())


    
