import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# def calculate_slope(point1, point2):
#     if point1[0] == point2[0]:
#         return float('inf')  # vertical line case
#     return (point1[1] - point2[1]) / (point1[0] - point2[0])

n, m = map(int, input().split())

locations = []
for _ in range(n):
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        locations.append((0, 0, 0))
    else:
        locations.append((x, y, 1))
# 1 means that the location is fixed, 0 means that the location is not fixed, couldn't think of a better solution

graph = dict()
for _ in range(m):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

# print("Read input")

should_stop = False
while not should_stop:
    should_stop = True
    for i, location in enumerate(locations):
        x, y, static = location
        if static:
            continue

        connections = graph[i + 1]
        delta_x = []
        delta_y = []

        for connection in connections:
            delta_x.append(locations[connection - 1][0] - x)
            delta_y.append(locations[connection - 1][1] - y)
        
        new_x = x + sum(delta_x) / len(delta_x)
        new_y = y + sum(delta_y) / len(delta_y)

        if abs(new_x - x) > 0.0001 or abs(new_y - y) > 0.0001:
            should_stop = False

        locations[i] = (new_x, new_y, static)


for location in locations:
    print(location[0], " ", location[1])