
def original_number(): #creates dictionary and assigns each letter of the alphabet its numerical value
	alphaoriginal = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 
				 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 
				 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
	print alphaoriginal
	
def shift(d):
	original_number()
	rote = int(raw_input("Please enter the shift number: "))
	alphashift = {}
	for key in d:
		shiftd = {str(d[key]):str(d[key+rote])}
		alphshift.update(shiftd)
	return alphashift
	


shift(original_number())
