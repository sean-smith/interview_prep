#!/usr/bin/python
# Tripadvisor Coding Challenge
# Sean Smith 10/19/2015

import sys


def parseFile(path):

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

	return map, robot_x, robot_y, max_x, max_y



map = [['.', '.', '.'],['R', 'O', 'T']]
max_x = 3
max_y = 2

# Start at robot's location and recurse in 4 directions
# Fill in a R in each unvisited square
def traverse(x, y):
	# print "x, y = "+str(x)+","+str(y)+"\ndot = "+map[y][x]

	if map[y][x] == 'T':
		return True
	elif map[y][x] == 'O':
		return False
	else:
		# map[y][x] = 'R'
		# print map
		path1 = False
		path2 = False
		path3 = False 
		path4 = False 
		if x > 0:
			path1 = traverse(x-1,y)
		if x < (max_x - 1):
			path2 = traverse(x+1,y)
		if y > 0:
			path3 = traverse(x,y-1)
		if y < (max_y - 1):
			path4 = traverse(x,y+1)
		return path1 or path2 or path3 or path4



def main():
	if len(sys.argv) != 2:
		print "Input a map file!\nrobotTraverse.py [path_to_file]"
		sys.exit()

	# map, robot_x, robot_y, max_x, max_y = parseFile(sys.argv[1])
	# print traverse(map, max_x, max_y, robot_x, robot_y)
	print traverse(0, 1)



main()
