"""
This is the skyline problem out lined here:
http://uva.onlinejudge.org/external/1/p105.pdf

Sean Smith
2015
swsmith@bu.edu

To run:
python3 skyline.py < in.txt

"""
import sys, heapq


class Building:
	def __init__(self, inp):
		line = inp.split()
		self.start = int(line[0])
		self.end = int(line[2])
		self.height	 = int(line[1])
	def __str__(self):
		return str(self.start)+" "+str(self.height)+" "+str(self.end)
	def __lt__(self, thing):
		return self.start < thing.start
	def __gt__(self, thing):
		return self.start > thing.start



list = [Building(line) for line in sys.stdin]

heapq.heapify(list)

print(list)
	


