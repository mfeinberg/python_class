import string

#Asks user for sentence to evaluate
sentence = raw_input("Please enter your sentence: ")

x = len(sentence)

#If statements to ensure sentence ends with a period
#and make string lower case because set() is case sensitive
if sentence[x-1].isalpha():
	sentence = string.lower(sentence)
	sentence = sentence + "."
else:
	sentence = string.lower(sentence)

x = len(sentence)

words = []
a = 0
y = 0

#While loop to split user-entered string into words
while y < x:
  while sentence[y].isalpha():
	y+=1
  words.append(sentence[a:y])
  a = y+1
  y=a
  
b = len(words)
c = 0

#While loop to remove and "" that may be in the set due to punctionation
#from the user-entered string 
while c < b-1:
	if words[c].isalpha():
		words[c]
	else:
		words.pop(c)
	c+=1
words_set = set(words)

print "Your sentence contains " + str(len(words_set)) + " unique words."
