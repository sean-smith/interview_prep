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


list = [(line.split()[0], (line.split()[1], line.split()[2]))  for line in sys.stdin]

heapq.heapify(list)


def skyline(length, building):
	s,r = building
	h,e = r


	#The start value
	s_1, r = heapq.pop(list)
	h_1, e_1 = r	
	if s == s_1 and h_1 > h:
		length, building  = skyline(length, (s_1, r))
	else:
		heapq.push((s_1, r))
		length += building[0]

	#The top portion
	s,r = building
	h,e = r
	s_1, r = heapq.pop(list)
	h_1, e_1 = r	
	if s_1 > e and h_1 > h:
		length, building  = skyline(length+(s_1-s), (s_1, r))
	else:
		heapq.push((s_1, r))
		length += building[0]


	#The down portion







print(skyline(0, heapq.pop(list)))
