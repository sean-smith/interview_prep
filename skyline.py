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
#list = [(12, (7, 16)), (14, (3, 25)), (19, (18, 22)), (23, (13, 29)), (24, (4, 28))]

heapq.heapify(list)


def skyline(length, building):
	
	length, building = up(length, building)
	print(length, building, list)
	length, building = middle(length, building)
	print(length, building, list)
	length, building = down(length, building)
	print(length, building, list)

	#GET NEXT IF NO NEXT RETURN HEIGHT
	if len(list) > 0:
		length = skyline(length, heapq.heappop(list))
		return length
	else:
		return length




def up(length, building):
	s = heapq.heappop(list)
	if building[0] == s[0] and s[1][0] > building[1][0]:
		return up(length, s)
	else:
		heapq.heappush(list, s)
		return length+building[1][0], building

def middle(length, building):
	#print(length, building, list)
	if len(list) == 0:
		return length+(building[1][1]-building[0]), building
	s = heapq.heappop(list)
	#if building starts before it ends and is taller
	if s[0] < building[1][1]:
		if s[1][0] > building[1][0]:
			return middle(length+(s[0]-building[0])+(s[1][0] - building[1][0]),s)
		else:
			x = middle(length, building)
			heapq.heappush(list, s)
			return x
	else:
		heapq.heappush(list, s)
		return length+(building[1][1]-building[0]), building


def down(length, building):
	print(length, building, list)
	if len(list) == 0:
		return length+building[1][0], building
	s = heapq.heappop(list)
	#if building starts before or equal to end and buidling ends past the end
	if s[0] <= building[1][1]:
		if s[1][1] > building[1][1]:
			l, b = middle(length+(building[1][0] - s[1][0]),(building[1][1],(s[1][0], s[1][1])))
			return l+b[1][0], b
		else:
			return down(length, building)
	else:
		heapq.heappush(list, s)
		return length+building[1][0], building




print(skyline(0, heapq.heappop(list)))
