import sys
# Python linked list implementation

class Node:
	def __init__(self, value, next = None):
		self.val = value
		self.next = next

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


# Reverses a linked list by flipping next pointers
def reverse(last, n):
	if n is None:
		return last
	else:
		tmp = Node(n.val, n.next)
		n.next = last
		return reverse(n, tmp.next)



n = Node("a");
insert(n, "b")
insert(n, "c")
insert(n, "d")
insert(n, "e")
print_list(n)
n = reverse(None, n)
print_list(n)