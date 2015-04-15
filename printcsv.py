#3) CSV Format

f = open('datatoformat.csv','r') 
lines = f.readlines() #reads lines in file and stores each line as an object in the list lines
f.close()

x = 0

while x < len(lines):
	format = str(lines[x])
	#format = format.replace(",","\t")
	#print format
	format_list = format.split(',')
	#print format_list
	y = 0
	z = 0

	if x == 0: #only works if four fields
		a = len(str(format_list[0]))
		b = len(str(format_list[1]))
		c = len(str(format_list[2]))
		d = len(str(format_list[3]))
		max_length = max(a,b,c,d)
	while y < len(format_list):
		if y != len(format_list)-1: 
			#while len(str(format_list[y])) < max_length:
				#format_list[y] = str(format_list[y]) + " "
			format_list[y] = str(format_list[y]).ljust(max_length)
		if x == 0 and y != len(format_list)-1:
			format_list[y] = str(format_list[y]) + ':'
			formated_string = str(format_list[y])
			formated_string = formated_string.replace(':','  |  ')
			print formated_string,
		elif y != len(format_list)-1:
			format_list[y] = str(format_list[y]) + ':'
			formated_string = str(format_list[y])
			formated_string = formated_string.replace(':','     ')
			print formated_string,
		else:
			formated_string = str(format_list[y])
			print formated_string
		y+=1
	x+=1
