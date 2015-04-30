#Write a program that doubles the square of a third of the reverse of the str() of the max of this list: [01,94,30,3.0,53].

#mas of the list: 94
#str -> '94'
#reverse -> '49'
#one thired -> 49/3 = 16.333
#squared -> 16.3333 ** 2 = 266.7777
#doubled -> 266.777 *2 = 533.5555

#max is a built-in
#str is a built-in

def rev(s):
  return s[::-1]
  
#we have a string, which is '49'
def thirdof(s):
  return float(s)/3

def squareof(num):
  return num * num

def doubleof(num):
  return num*2

def main(l):
  #do the work of computing the final result here using the functions above
  max_of_list = max(l)
  max_as_str = str(max_of_list)
  rev_max_as_str = rev(mas_as_str)
  #could continue this way but so cumbersome...

def main_alex_way(l)
  funcs = [max,str,rev,thirdof,squareof,doubleof]
  temp = l
  for f in funcs:
    temp = f(temp)
  print temp
  #could also do it as a while loop
  temp = l
  while funcs:
    f = funcs.pop(0)
    temp = f(temp) 

#program starts here
#l = [01,94,30,3.0,53]
l = raw_input('Enter a comma-separated list of numbers: ')
l = [float(num) for num in l.split(,)] #doesn't work because not everything should be a float...would have to additional parsing
#to determine if float...like if '.' in 
main(l)
