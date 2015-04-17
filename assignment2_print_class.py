f = open('mock_data.csv')
content = f.readlines()
f.close()
header = content[0]
data = content[1:]
width = 15

#print out header in a nice way
header_titles = header.split(",")
print '| '.join(title.ljust(width).upper for title in header_titles)

for line in data:
	line_values = line.split(',')
	print '  '.join(value.ljust(width) for value in line_values)
