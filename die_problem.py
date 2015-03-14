"""
Die Problem that I got at the athena interview

Sean Smith 

Given 
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
	def moveEast(self):
		self.positionx += 1
		self.cost += self.right
		self.path += ["W"]
		self.top = self.left
		self.left = self.bottom
		self.bottom = 7 - self.top
		self.right = 7 - self.left


def solve(Die):
	if Die.positionx == 3 and Die.positiony == 2:
		return Die
	elif Die.positionx < 3 and Die.positiony < 2:
		path1 = solve(Die.moveEast())
		path2 = solve(Die.moveNorth())

		return min(path1, path2, key=lambda n: Die.cost)





print(solve(Die(3, 2, 1)))