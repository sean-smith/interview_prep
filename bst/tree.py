import Queue

class Node:

	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


def insert(n, val):
	if n is None:
		return Node(val)
	elif val > n.val:
		n.left = insert(n.left, val);
		return n
	elif val < n.val:
		n.right = insert(n.right, val);
		return n


def bft(n):
	q = Queue.Queue()
	q.put(n)
	while not q.empty():
		q.get(n)
		print n.val
		if n.left is not None:
			q.put(n.left)
		if n.right is not None:
			q.put(n.right)

n = Node(5)
n = insert(n, 6)
n = insert(n, 7)
n = insert(n, 8)
n = insert(n, 4)
n = insert(n, 3)
n = insert(n, 2)
n = insert(n, 1)
bft(n)