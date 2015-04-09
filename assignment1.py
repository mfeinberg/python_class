sentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

#email suggestion
words = [sentence[:6], sentence[7:9], sentence[10:16], sentence[17:24], sentence[25:27], sentence[28:30], sentence[31:39], sentence[41:46], sentence[47:49], sentence[50:58], sentence[59:66], sentence[67:69], sentence[70:72],sentence[73:78]] 
words_set = set(words)
len(words_set)

#google's advice
words2 = sentence.split()
words2_set = set(words2)
len(words2_set)

#attempt using  loop 
sentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

x = len(sentence)

words3 = []

a = 0
y = 0
while y < x:
  while sentence[y].isalpha():
	y+=1
  words3.append(sentence[a:y])
  a = y+1
  y=a

print words3

b = len(words3)
print b
c = 0
while c < b-1:
	if words3[c].isalpha():
		print "alpha",
		print c
	else:
		words3.pop(c)
		print words3
	c+=1
	
	
words3_set = set(words3)

print words3_set

print len(words3_set)
