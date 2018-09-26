#pyex5.py



import sys

wordlength = [] # must declare empty list

for word in sys.stdin:
		length = len(word) -1
		wordlength[length] += 1
