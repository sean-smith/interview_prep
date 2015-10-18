
class node:
	def __init__(value, next=None):
		self.value = value
		self.next = next


def hash(obj, size):
	return (ord(obj) - ord('a')) % size

#tells if all letters are unique
#1.1
def unique(string):
	list = [0]*26
	string = string.lower()
	for each in string:
		h = hash(each, 26)
		if list[h] == 1:
			return False
		else:
			list[h] = 1
	return True

print "isUnique(sjkdjfskjdf) = " + str(unique("sjkdjfskjdf"))
print "isUnique(abcdefghijklmnop) = " + str(unique("abcdefghijklmnopqrstuvwxyz"))


# Reverses a string
# 1.2 v5
# I'm going to write a C implementation as well 
# as I think this is a better question for a low level language
def reverse(str):
	new = ""
	for i in range(len(str)-1, -1, -1):
		new += str[i]
	return new

print "reverse(sjkdjfskjdf) = " + str(reverse("sjkdjfskjdf"))

# Figures out if one string is a permutation of another
# 1.3v5 (or 1.2v6)
def permutation(st1, st2):
	st1 = st1.lower()
	st2 = st2.lower()
	list = [0]*26
	for letter in st1:
		h = hash(letter, 26)
		list[h] += 1
	for letter in st2:
		list[hash(letter, 26)] -= 1
		if list[hash(letter, 26)] < 0:
			return False
	return len(st1) == len(st2)

print "permutation('fsjkdjfskjd', 'sjkdjfskjdf') = " + str(permutation("fsjkdjfskjd", "sjkdjfskjdf"))


#replaces spaces in a string by %20 similar to urlencode
#1.4
def spaces(str):
	length = len(str)
	i = 0
	while i < length:
		each = str[i]
		if each == " ":
			str = str[:i]+"%20"+str[i+1:]
			i += 3
			length += 2
		else:
			i+=1
	return str

#outputs a string with the first letter of the original string and a number of character
#ccbaaass
#c2ba3s2
#1.5
def compress(string):
	final = ""
	if len(string) == 1:
		return string+'1'
	length = len(string)
	i = 1
	last = string[0]
	count = 1
	while i < length:
		current = string[i]
		if current == last:
			count += 1
		else:
			final += last+str(count)
			count = 1
			last = current
		i+=1
	return final+current+str(count)



print "compress('ccbaaassssssnnfksss') = " + compress('ccbaaassssssnnfksss')