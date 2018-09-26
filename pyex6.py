#pyex6.py

import sys

wordlength = {} # declare an empty dictionary

for word in sys.stdin:
		length = len(word) - 1 # length will be a key
		if (wordlength.has_key(length)): # has_key only good in Python 2
			wordlength[length] += 1 # if the code has seen the length, the value is incremented by 1
		else:
			wordlength[length] = 1 # if the code has not seen the input wordlength, it will create that pair


for i in wordlength.keys(): #no need to sort keys, they are already sorted unlike perl
	print '%i: %i' % (i, wordlength[i]) # print integer: another integer. The ints being printed are in the () 
