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
