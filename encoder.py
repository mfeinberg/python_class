#DOES NOT YET TAKE INTO ACCOUNT CAP V NON CAP
def original_number(): #creates dictionary and assigns each letter of the alphabet its numerical value
	alphaoriginal = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', #starting at 0 necessary for shift
				 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 
				 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
	return alphaoriginal
	
def shift(d):
	rote = int(raw_input("Please enter the shift number: ")) #gets rotation number
	alphashift = {}
	for key in d:
		shiftd = {str(d[key]):str(d[((key+rote) % 26)])} # % function used because key+rote>25 not in range and breaks
		alphashift.update(shiftd)
	return alphashift 
	


ashift = shift(original_number()) #creates shifted dictionary

cipher = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

cipher2 = "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna htyl.\nRkcyvpvg vf orggre guna vzcyvpvg.\nFvzcyr vf orggre guna pbzcyrk.\nPbzcyrk vf orggre guna pbzcyvpngrq.\nSyng vf orggre guna arfgrq.\nFcnefr vf orggre guna qrafr.\nErnqnovyvgl pbhagf.\nFcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.\nNygubhtu cenpgvpnyvgl orngf chevgl.\nReebef fubhyq arire cnff fvyragyl.\nHayrff rkcyvpvgyl fvyraprq.\nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.\nGurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.\nNygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.\nAbj vf orggre guna arire.\nNygubhtu arire vf bsgra orggre guna *evtug* abj.\nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\nVs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"

deciphered = []
for letter in cipher2:
	if letter in ashift:
		deciphered.append(ashift[letter])
	else:
		deciphered.append(letter)
		
print ''.join(i for i in deciphered)
