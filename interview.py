"""
Sean Smith

Athena technical interview 


Problem:
Given the probabilities of scoring each point as follows:
P[0] = .5
P[1] = .3
P[2] = .2

Give the probability of scoring different values after 5 rounds of the above probability.

Then they extended it to give the top ten probabilities and the probability given any probability distribution.
"""

import heapq

p0 = .5
p1 = .3
p2 = .2


def p(s, r):
	if r ==1:
		if s== 1:
			return .3
		if s== 2:
			return .2
		if s == 0:
			return .5
		if s<0 or s>2:
			return 0
	elif r > 1:
		return (p(s,r-1)*p0 + p(s-1, r-1)*p1 + p(s-2, r-1)*p2)

"""
for i in range(0,11):
	print(i, p(i, 5))
"""


def topTen(N):
	h = []
	for a in range(0, 2*N+1):
		for b in range(0, 2*N+1):
			q = Q(a,b,N)
			if len(h) < 10:
				heapq.heappush(h, (q, (a,b)))
			elif len(h) == 10:
				heapq.heappush(h, (q, (a,b)))
				heapq.heappop(h)
	return sorted(h, key=lambda n: n[0])

def Q(a,b,N):
	return p(a,N)*p(b,N)



l = [.25, 0, .05, .3,0,0, .1, .2, .1]


def anyP(s,r,l):
	if r == 1:
		if s<0 or s>=len(l):
			return 0
		else:
			return l[s]
	elif r > 1:
		sum = 0
		for i in range(len(l)):
			if l[i] > 0:
				sum += anyP(s-i, r-1, l)*l[i]
		return sum

for i in range(0, (len(l)-1)*5+1):
	print(i, anyP(i, 5, l))


