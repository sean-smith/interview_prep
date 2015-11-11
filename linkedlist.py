import sys
# Python linked list implementation

class Node:

	def __init__(self, value):
		self.val = value
		self.next = None

def print_list(n):
	while n.next is not None:
		sys.stdout.write(n.val+" -> ")
		n = n.next
	sys.stdout.write(n.val)
	print

def insert(n, val):
	while n.next is not None:
		n = n.next
	n.next = Node(val)


# To do
def reverse(last, n):
	if n.next is None:
		n.next = last
		return n
	else:
		tmp = n.next
		n.next.next = n
		n.next = last
		reverse(n, tmp)





n = Node("a");
insert(n, "b")
insert(n, "c")
insert(n, "d")
insert(n, "e")
print_list(n)
n = reverse(None, n)
print_list(n)