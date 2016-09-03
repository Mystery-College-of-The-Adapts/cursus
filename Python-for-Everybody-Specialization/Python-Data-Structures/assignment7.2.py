"""a program to prompt for a file name, and then read through
the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475"""

fname = raw_input('Enter a file name:')
try:
	f = open(fname)
except:
	print 'File cannot be opened:', fname

searchline = 'X-DSPAM-Confidence:'
foundLine=''

for line in f:
	line = line.strip()
	if line.startswith(searchline):
		foundLine = line

index = (foundLine.find(" "))
num = float(foundLine[index:].strip(" "))


print foundLine
print num

