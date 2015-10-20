#!/usr/bin/python
# Tripadvisor Coding Challenge
# Sean Smith 10/19/2015

import sys



if len(sys.argv) != 2:
	print "Input a map file!\nrobotTraverse.py [path_to_file]"
	sys.exit()

path = sys.argv[1]

f = open(path, "r")

max_x = 3
max_y = 2

map = [[0 for x in range(max_x)] for x in range(max_y)] 

# Initialize 2d array for map
# x, y values are indexed from upper left corner
for y, line in enumerate(f):
	for x, dot in enumerate(line):
		if dot != '\n':
			print "x, y = "+str(x)+","+str(y)+" dot = "+dot
			map[y][x] = dot
		if dot == 'R':
			robot_x = x
			robot_y = y

f.close()

print map

print "robot_x = "+str(robot_x)+" robot_y = "+str(robot_y)



def traverse(x, y):
	print "x, y = "+str(x)+","+str(y)+"\ndot = "+map[y][x]
	if (x < max_x and y < max_y and x >= 0 and y >= 0):
		if map[y][x] == 'T':
			return True
		if not (map[y][x] == 'O' or map[y][x] == 'R'):
			map[y][x] = 'R'
			traverse(x+1,y)
			traverse(x-1,y)
			traverse(x,y+1)
			traverse(x,y-1)


print traverse(robot_x, robot_y)
print map

