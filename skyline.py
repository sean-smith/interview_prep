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



def skyline(item):
	s,h,e = item


	#The start value	
	item = heapq.pop(list)
	if item.start == s and item.height > height:
		print()


	#The top portion


	#The down portion







#print(skyline(heapq.pop(list)))
