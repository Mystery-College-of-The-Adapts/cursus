fhand = open('loremIpsum.txt','r')
count = 0

for line in fhand:
	count += 1

print 'Line Count:', count 

# Save the read whole file in a string

a = open('loremIpsum.txt')
for line in iter(a):
	print line 

print "Searching Through a File:"
f = open('loremIpsum.txt')
for line in f:
	line = line.rstrip()
	if line.startswith('L'):
		print line 

# Skipping with Continue
print "Skipping With Continue:\n"
f = open('loremIpsum.txt')
for line in f:
	line = line.rstrip()
	if line.startswith('L'):
		continue

	print line 


fname = raw_input('Enter the file name:')
try:
	fhand = open(fname)

except:
	print 'File cannot be opened:', fname
	exit()

count = 0
for line in fhand:
	if line.startswith('Le'):
		count += 1
print "There were", count, 'Le lines in ', fname
