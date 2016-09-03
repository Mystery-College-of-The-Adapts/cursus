fhand = open('loremIpsum.txt','r')
count = 0

for line in fhand:
	count += 1

print 'Line Count:', count 

# Save the read whole file in a string

for line in iter(fhand):
	print line 

fhand.close()
