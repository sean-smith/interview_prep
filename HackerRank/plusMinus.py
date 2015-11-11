# Enter your code here. Read input from STDIN. Print output to STDOUT
 
n = float(raw_input())
list = raw_input().split()
positive = 0
negative = 0
zeroes = 0

for num in list:
	num = int(num)
	if num > 0:
		positive += 1
	elif num < 0:
		negative += 1
	else:
		zeroes += 1

print( 1.0 * positive / n )
print( 1.0 * negative / n)
print( 1.0 * zeroes / n)