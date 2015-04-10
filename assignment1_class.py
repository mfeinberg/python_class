origingal = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."
copy = origingal[:] #an independent copy of original
copy = copy.lower() #set() is case sensitive so make all letters same case
#Goal: get a count of unique words

#Step 1: Trim non-word punctuation

copy = copy.replace(";","").replace(".","") #can chain the .replace()

#string now looks like "Thrift is poetic because it is creative waste is unpoetic because it is waste"

#Step 2: split into list of words using split()
#now have list of the words

words = copy.split()

#Step 3: convert list to set by using set(l)

word_set = set(words)

#Step 4: find length of set by calling len() on set

print len(word_set)


#Task 2 use words as a basis for reconstructing the original sentence
' '.join(words) #list of words now joined back into a single string

#Insert the punctuation back to where it was
semi_index = origingal.index(';') #finds position of ; in original sentence
dot_index = origingal.index('.')

copy_list = list(copy)
copy_list.insert(semi_index,';') #just modifying the list, so cannot be chained
copy_list.insert(dot_index,'.')
print ''.join(copy_list).capitalize()

#capitalize the first sentence

#assert that the original string == copy

