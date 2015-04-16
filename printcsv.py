#Assignment 2: 3) CSV Format

f = open('datatoformat2.csv','r') 
lines = f.readlines() #reads lines in file and stores each line as an object in the list lines
f.close()

for x in range (0,len(lines)):
	format = str(lines[x])
	format_list = format.split(',')
	if x == 0:
		num_fields = len(format_list) #number of fields in the csv file
		field_list = []
		for num in range (0, num_fields):
			field_list.insert(num, len(str(format_list[num])))
		max_length = max(field_list) #finds field/column header with the longest length
	for y in range (0, len(format_list)):
		format_list[y] = str(format_list[y]).ljust(max_length) #left justifies each item in the list, padding with spaces as needed so each entry has the same length
		if x == 0 and y != len(format_list)-1:
			format_list[y] = str(format_list[y]) + '  |  ' #adds | to neatly separate field/column headers
			formated_string = str(format_list[y])   
			print formated_string,
		elif y != len(format_list)-1:
			format_list[y] = str(format_list[y]) + '     ' #adds a few spaces for formatting purposes
			formated_string = str(format_list[y])
			print formated_string,
		else:
			formated_string = str(format_list[y])
			print formated_string
