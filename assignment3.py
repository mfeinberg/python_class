#Write a program that doubles the square of a third of the reverse of the str() of the max of this list: [01,94,30,3.0,53].

assigned_list = [01,94,30,3.0,53]

def find_max(list_input): #function that finds the max in a list of numbers
	print max(list_input)
	return max(list_input)
	
def convert_to_string(numerical_input): #function that converts a number to a string
	print str(numerical_input)
	return str(numerical_input)

def reverse_string(string_input): #function that reverses a string
	print string_input[::-1]
	return string_input[::-1]

def one_third(number_to_divide): #function that divides a number by 3
	print float(number_to_divide) / 3
	return float(number_to_divide) / 3

def f_square(number_to_square): #function that squares a number
	print number_to_square ** 2
	return number_to_square ** 2
	
def f_double(number_to_double): #function that doubles a number
	print number_to_double * 2
	return number_to_double * 2
	
print f_double(f_square(one_third(reverse_string(convert_to_string(find_max(assigned_list))))))
