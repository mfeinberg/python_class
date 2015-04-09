import string
import re

#Asks user for sentence to evaluate
sentence = raw_input("Please enter your sentence: ")

#Makes all characters lower case
sentence = string.lower(sentence)

#Removes all punctionation from the string
sentence = re.sub('[.]','',sentence)
sentence = re.sub('[:]','',sentence)
sentence = re.sub('[;]','',sentence)
sentence = re.sub('[?]','',sentence)
sentence = re.sub('[(]','',sentence)
sentence = re.sub('[)]','',sentence)
sentence = re.sub('[!]','',sentence)

#Splits string into list and then turns list into set
words = set(sentence.split())

#Prints number of unqiue words
print "Your sentence contains " + str(len(words)) + " unique words."
