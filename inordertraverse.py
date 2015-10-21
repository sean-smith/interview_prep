# Traverse a 2D array 
# Go in order from 1 - 9
# Return the path of traversal

"""
1 0 3 0 0
0 2 0 4 0
0 7 0 5 0
8 0 6 0 0
0 9 0 7 0
"""

r1 = [1, 0, 3, 0, 0]
r2 = [0, 2, 0, 4, 0]
r3 = [0, 7, 0, 5, 0]
r4 = [8, 0, 6, 0, 0]
r5 = [0, 9, 0, 7, 0]

arr = [r1, r2, r3, r4, r5]

max_x = len(arr[0])
max_y = len(arr)

def traverse(x, y, current, path):
    print path, current
    if current == 9:
        return path
    if x > 0:
        if arr[y][x - 1] == current + 1:
            path += [(x-1, y)]
            return traverse(x - 1, y, current+1, path)
    if y > 0:
        if arr[y - 1][x] == current + 1:
            path += [(x, y-1)]
            return traverse(x, y-1, current+1, path)
    if x < max_x - 1:
        if arr[y][x + 1] == current + 1:
            path += [(x+1, y)]
            return traverse(x + 1, y, current+1, path)
    if y < max_y - 1:
        if arr[y + 1][x] == current + 1:
            path += [(x, y+1)]
            return traverse(x, y+1, current+1, path)
    if x < max_x - 1 and y < max_y - 1:
        if arr[y + 1][x + 1] == current + 1:
            path += [(x+1, y+1)]
            return traverse(x + 1, y+1, current+1, path)
    if x > 0 and y > 0:
        if arr[y - 1][x - 1] == current + 1:
            path += [(x-1, y-1)]
            return traverse(x - 1, y-1, current+1, path)
    if x > 0 and y < max_y - 1:
        if arr[y + 1][x - 1] == current + 1:
            path += [(x-1, y+1)]
            return traverse(x - 1, y+1, current+1, path)
    if x < max_x - 1 and y > 0:
        if arr[y - 1][x + 1] == current + 1:
            path += [(x+1, y-1)]
            return traverse(x + 1, y-1, current+1, path)
        
        
        
print traverse(0, 0, 1, [(0,0)])