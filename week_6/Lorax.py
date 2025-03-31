import math
x,y = map(int,input().split())

square_x1, square_y1, square_x2, square_y2 = map(int,input().split())

def gcf(a,b):
    while a:
        a %= b
        if a == 0:
            return b
        a,b = b,a

gcf = gcf(x,y)
factored_x = x // gcf 
factored_y = y // gcf
# These are like a unit in the x and y direction

def is_point_in_square(x,y):
    return square_x1 <= x <= square_x2 and square_y1 <= y <= square_y2

first_point = (0+factored_x,0+factored_y)
last_point = (x-factored_x,y-factored_y)

# print(f"First point: {first_point}")
# print(f"Last point: {last_point}")

if is_point_in_square(*first_point) and is_point_in_square(*last_point):
    print("Yes")

else:
    #Find the first missing point
    if is_point_in_square(*first_point):
        #If the first point is in the square, the last point must be out of the square
        print("No")
        # one_after_square_x = math.ceil(square_x2/factored_x)*factored_x
        # one_after_square_y = math.ceil(square_y2/factored_y)*factored_y
        one_after_square_x = ((square_x2 - square_x2 // factored_x)+1) * factored_x
        one_after_square_y = ((square_y2 - square_y2 // factored_y)+1) * factored_y
        print(one_after_square_x,one_after_square_y)
    else:
        #If the first point is missing we just print the first point
        print("No")
        print(*first_point)