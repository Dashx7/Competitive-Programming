from collections import defaultdict, deque
n,m = map(int,input().split())

adjacency_list = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    bottom, top = map(int,input().split())
    adjacency_list[bottom].append(top)
    indegree[top] += 1

queue = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)
result = []

while queue:
    current = queue.popleft()
    result.append(current)
    for neighbor in adjacency_list[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(result) == n:
    print("\n".join(map(str, result)))
else:
    print("IMPOSSIBLE")


