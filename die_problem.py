"""
Die Problem that I got at the athena interview

Sean Smith 
swsmith@bu.edu	
2015

Given a die in a 3x2 matrx find the lowest cost path from (0,0) to (3,2)
The cost of a path is facing up value once you move
"""


class Die:
	def __init__(self, left, top, front):
		self.left = left
		self.right = 7 - left
		self.top = top
		self.bottom = 7 - top
		self.front = front
		self.back = 7 - front
		self.cost = 0
		self.path = []
		self.positionx  = 0
		self.positiony  = 0
	def moveNorth(self):
		self.positiony += 1
		self.cost += self.front
		self.path += ["N"]
		temp = self.top
		self.top = self.back
		self.front = temp
		self.back = 7 - self.front
		self.bottom = 7 - self.top
		return self
	def moveEast(self):
		self.positionx += 1
		self.cost += self.right
		self.path += ["W"]
		self.top = self.left
		self.left = self.bottom
		self.bottom = 7 - self.top
		self.right = 7 - self.left
		return self
	def __str__(self):
		return str(self.path)


def solve(Die):
	path1 = None
	path2 = None
	if Die.positionx == 3 and Die.positiony == 2:
		return Die
	if Die.positionx < 3:
		path1 = solve(Die.moveEast())
	if Die.positiony < 2:
		path2 = solve(Die.moveNorth())
	if path1 is None:
		return path2
	if path2 is None:
		return path1
	else:
		return min(path1, path2, key=lambda n: n.cost)




print(solve(Die(3, 2, 1)))