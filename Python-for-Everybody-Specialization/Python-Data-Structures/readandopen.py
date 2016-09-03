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
	if line.startswith('L'):
		print line 
