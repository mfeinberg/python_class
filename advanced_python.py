#!/usr/bin/env python

# splat operator 

card = ('Queen','Spades')

print "{} of {}".format(card[0], card[1])
print "{} of {}".format(*card) #equivalent to above; if have function that takes in list, iterates through the items

# *args, **kwargs #methods to pass in an arbitrary number of arguments to a function
# names are arbitrary, single * is no key, **kw is kew word

def print_args(*args):
	for arg in args:
		print arg,
	print '\n'
		
print_args('one','two','three')
print_args('one','two','three','four')

def print_kwargs(**kwargs):
	for k in kwargs:
		print k, kwargs[k]
		
print_kwargs(one="1", two="two", three="3")

# lambda is an anonymous function/a function without a name, can only take one argument 
# functional programming tool

l = [('b',4),('a',2),('b',0),('b',-3)]
# sort in ascending order the [0] index of each tuple

def custom_sort(t):
	return t[0],t[1]

print sorted(l,key=custom_sort)
print sorted(l,key=lambda x: (x[0], x[1]))

# scoping
# LEGB - local, enclosed, global, built-in
# lexical/static scoping vs dynamic scoping
# code determines scope of a name in a function

a = 4

def test():
	#print a #can't do this get an error about referencing a variable before it is assigned because it parses the function as a whole
	a = 2
	print locals() #none
	print a
	global b #can define a variable as global, but probably shouldn't do it 
	b = 2
	
test()
print locals()
print a
print b

# closures
# way of protecting some data

def outer():
	phrase = 'is the coolest.'
	
	def inner(name):
		print ' '.join([name,phrase])
	
	return inner
# outer function and some inner function. outer function has data inside of it
# inner function because of scoping can refer to data from outer function
# reference to data persists, even after function is over

sentence_generator = outer() #returns inner to sentence_generator
sentence_generator('matthew')

#in python things are deleted after reference disappears
