import Queue

q = Queue.Queue()

q.put("hi")
q.put(3)
print q.get()
print q.get()

print q

l = []

l.append("hi")

print l.pop()
print l