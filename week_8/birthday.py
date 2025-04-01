from collections import defaultdict


def process_input():
    results = []
    numV = []
    while True:
        # Read first line
        try:
            header = input().strip().split()
        except EOFError:
            break
        numV.append(int(header[0]))
        num_lines = int(header[1])
        if num_lines == 0:
            break

        test_case = []
        for _ in range(num_lines):
            try:
                line = input().strip().split()
                test_case.append(tuple(map(int, line)))
            except EOFError:
                break

        results.append(test_case)

    return numV, results





# This class represents an undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
        self.b = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    '''A recursive function that finds and prints bridges
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree'''

    def bridgeUtil(self, u, visited, parent, low, disc):

        # Mark the current node as visited and print it
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])

                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[v] > disc[u]:
                    self.b += 1


            elif v != parent[u]:  # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])

    # DFS based function to find all bridges. It uses recursive
    # function bridgeUtil()
    def bridge(self):

        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)

def solve():
    vert, testCases = process_input()

    count = 0
    for case in testCases:
        graph = Graph(vert[count])
        count += 1
        for i in range(len(case)):
            graph.addEdge(case[i][0],case[i][1])
        graph.bridge()
        if graph.b == 0:
            print("No")
        else:
            print("Yes")


    return

solve()