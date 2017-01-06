"""a program to read through a file and print the contents of the
file (line by line) all in upper case"""

# Open the file 

fname = raw_input('Enter the file name:')
try:
	f = open(fname)

except:
	print 'File cannot be opened:', fname
	exit()

for line in f:
	line = line.rstrip()
	print line.upper()