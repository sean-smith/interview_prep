# Enter your code here. Read input from STDIN. Print output to STDOUT

s = list(raw_input())

# reverse letters of each word
def swap(s, i, j):
	while (i < len(s) and j > 0 and j > i):
		tmp = s[j]
		s[j] = s[i]
		s[i] = tmp
		i += 1
		j -= 1
	return s

# reverse string
i = 0
j = len(s) - 1
s = swap(s, i, j)

print s


start = 0
for end in range(len(s)):
	if s[end] == ' ':
		s = swap(s, start, end - 1)
		start = end + 1
		
s = swap(s, start, end)



print ''.join(s)