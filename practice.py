"""
Sean Smith

Previous Athena interview question:

write a program that will analyse the string.... 

char str[90]="my brother is taller than me@1233334. I always a short man,but smart than him"; 

1)Remove spaces between words, 
2)Find the longest word in the String, 
3)Search and count the number of letters"e" in the string 4)Extact the number of integers in string 
5)Extract the number of doubles in string 
6)Extract the number of words in string 
7)Identify the number of sentences in the String.
"""



import re
string  = "my brother is taller than me@122344.0 I always a short man,but smart than him"
string2 = "Freud qualified as a doctor of medicine at the University of Vienna in 1881,[3] and then carried out research into cerebral palsy, aphasia and microscopic neuroanatomy at the Vienna General Hospital.[4] Upon completing his habilitation in 1895, he was appointed a docent in neuropathology in the same year and became an affiliated professor (professor extraordinarius) in 1902.[5][6]"
def whitespace(string):
	list = string.split()
	for each in list:
		print(each, end="")
	print(list)

def longest(string):
	list = string.split()
	max = 0
	for word in list:
		if len(word) > max:
			longest = word
			max = len(word)
	print(longest)

def numE(string):
	string = string.lower()
	sum = 0
	for letter in string:
		if letter == 'e':
			sum+=1
	return sum

def integers(string):
	ints = re.split(r"([0-9]*)", string)
	for each in ints:
		if re.match(r"^([1-9][0-9]*)$", each):
			return int(each)

def doubles(string):
	ints = re.split(r"([1-9][0-9]*\.[0-9][0-9]*)", string)
	print(ints)
	for each in ints:
		if re.match(r"^([1-9][0-9]*\.[0-9]*)$", each):
			return float(each)


def numWords(string):
	ints = re.split(r"(,|\.|\s)", string)
	print(ints)
	sum = 0
	for each in ints:
		if re.match(r"^[a-zA-Z]*$", each):
			sum+=1
	return sum

def numSentences(string):
	ints = [x for x in re.split(r"(\.)", string) if not x == " "]
	print(ints)
	return len(ints) - 2






if(__name__=="__main__"):
	print(numSentences(string2))