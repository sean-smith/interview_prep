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


list = [(int(line.split()[0]), (int(line.split()[1]), int(line.split()[2])))  for line in sys.stdin]

heapq.heapify(list)


def skyline(length, building):
	

	length, building = up(length, building)
	length, building = top(length, building)
	length, building = down(length, building)

	#GET NEXT IF NO NEXT RETURN HEIGHT




def up(length, building):
	s = heapq.pop(list)
	if building[0] == s[0] and s[1][0] > building[1][0]:
		return up(s)
	else:
		heapq.push(list, s)
		return building[0], building

def middle(length, building):
	s = heapq.pop(list)
	#if building starts before it ends and is taller
	if s[0] > building[1][1] and s[1][0] > building[1][0]
		return up(s)
	else:
		heapq.push(list, s)
		return building[0], building


def down()




print(skyline(0, heapq.pop(list)))
