#pyex8.py
import re


#Alternatively,input_file = open(args[1], "r")
input_file = open("cs176roster.webadvisor.txt", "r")

whole_thing = input_file.read() # whole_thing = big string


regex= re.compile(r'.+?, .+\n[0-9]{7}') # find regular expression
names = regex.findall(whole_thing)

for student in names:
	student = re.sub(r'\n', ', ', student)
	print(student)
