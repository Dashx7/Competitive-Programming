class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
    def __repr__(self):
        return f"TreeNode(value={self.value}, children={self.children})"

n = int(input())
g = [[] for _ in range(n)]
children = [[] for _ in range(n)]

for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

visited = [False] * n
def dfs(node):
    visited[node] = True
    for neighbor in g[node]:
        if not visited[neighbor]:
            children[node].append(neighbor)
            dfs(neighbor)

dfs(0)

cache = [[0,0] for _ in range(n)]
def dp(node):
    for child in children[node]:
        dp(child)
        cache[node][1] += max(cache[child])
    for child in children[node]:
        cache[node][0] = max(cache[node][0], cache[node][1] - max(cache[child]) + 1 + cache[v][1])

        
dp(0)
print(max(cache[0]))
# print(cache)
    
# Matching nodes