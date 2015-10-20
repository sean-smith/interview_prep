#!/usr/bin/python

# Tripadvisor Coding Challenge
# Sean Smith 10/20/2015

import sys

class RobotTraverse:

	def __init__(self, path):
		self.map, self.start_x, self.start_y = self.parseFile(path)
		self.max_x = self.getMaxX()
		self.max_y = self.getMaxY()

	# A wrapper to run traverse
	def main(self):
		# Set starting position to unvisited
		self.map[self.start_y][self.start_x] = '.'

		# Run the main traverse Algorithm and print yes or no
		if self.traverse(self.start_x, self.start_y):
			print "yes"
		else:
			print "no"


	# Read in file and return a 2d array
	# return robot start and 
	def parseFile(self, path):

		try:
			f = open(path, "r")
		except IOError as e:
			print "Invalid path to file... "+str(e.strerror)
			sys.exit();

		map = []

		robot_x = 0
		robot_y = 0

		# Initialize 2d array for map
		# x, y values are indexed from upper left corner
		for y, line in enumerate(f):
			row = []
			for x, dot in enumerate(line):
				if dot != '\n':
					row += dot
				if dot == 'R':
					robot_x = x
					robot_y = y
			map += [row]

		f.close()

		if (not robot_x or not robot_y):
			print "Map file doesn't have a start location (R)... exiting"
			sys.exit();

		# Robot's starting location and complete map
		return map, robot_x, robot_y

	# size of the map
	def getMaxX(self):
		return len(self.map[0])

	def getMaxY(self):
		return len(self.map)


	# Start at robot's location and recurse in 4 directions
	# Fill in a V in each visited square
	# Return false when you go out of bounds, hit an obstacle or return to visited square
	# return true when you hit the target
	def traverse(self, x, y):
		if x < 0 or y < 0 or x >= self.max_x or y >= self.max_y:
			return False
		if self.map[y][x] == 'O':
			return False
		if self.map[y][x] == 'T':
			return True

		if self.map[y][x] == '.':
			self.map[y][x] = 'V'		# Mark the square as visited

			# Move in 4 directions
			east = self.traverse(x-1,y)
			west = self.traverse(x+1,y)
			north = self.traverse(x,y - 1)
			south = self.traverse(x,y+1)

			return east or west or north or south


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Please supply a map file\nrobotTraverse.py [path_to_file]"
		sys.exit()

	traverse = RobotTraverse(sys.argv[1])
	traverse.main()