from collections import deque
r,c = map(int,input().split())
ocean = []
for _ in range(r):
    ocean.append(list(input()))

# print(ocean)

tests = int(input())
def add_to_queue(x,y,distance, left = False):
    if x >= 0 and x < r and y >= 0 and y < c:
        if left:
            queue.appendleft((x,y,distance))
        else:
            queue.append((x,y,distance+1))

for problem in range(tests):
    x1,y1,x2,y2 = map(int,input().split())
    x1 -=1; y1 -=1; x2 -=1; y2 -=1
    queue = deque()
    queue.append((x1,y1,0))
    visited = {}

    while queue:
        x,y,distance = queue.popleft()
        if x == x2 and y == y2:
            print(distance)
            break
        else:
            if (x,y) not in visited: # Prevents revisiting the same cell
                visited[(x,y)] = True
                # print(f"Checking {x+1},{y+1}")
                if ocean[x][y] == '0':
                    add_to_queue(x-1,y,distance, True)
                else:
                    add_to_queue(x-1,y,distance)

                if ocean[x][y] == '1':
                    add_to_queue(x-1,y+1,distance, True)
                else:
                    add_to_queue(x-1,y+1,distance)

                if ocean[x][y] == '2':
                    add_to_queue(x,y+1,distance, True)
                else:
                    add_to_queue(x,y+1,distance)

                if ocean[x][y] == '3':
                    add_to_queue(x+1,y+1,distance, True)
                else:
                    add_to_queue(x+1,y+1,distance)
                
                if ocean[x][y] == '4':
                    add_to_queue(x+1,y,distance,True)
                else:
                    add_to_queue(x+1,y,distance)

                if ocean[x][y] == '5':
                    add_to_queue(x+1,y-1,distance,True)
                else:
                    add_to_queue(x+1,y-1,distance)

                if ocean[x][y] == '6':
                    add_to_queue(x,y-1,distance,True)
                else:  
                    add_to_queue(x,y-1,distance)
                
                if ocean[x][y] == '7':   
                    add_to_queue(x-1,y-1,distance,True) 
                else:
                    add_to_queue(x-1,y-1,distance)
                # print(f"Queue: {queue}")