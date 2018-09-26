#pyex4.py
# Create, save and run pyex4.py to see if strings of standard input are “chomped” by Python by default. Try the string len() and rstrip() methods.

import sys

for line in sys.stdin:
	#print len(line)
	print(len(line))
	line = line.rstrip() #like Perl chomp, returns string with rightmost char removed
	print(line)
