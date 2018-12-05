import numpy as np
from datetime import datetime as dt

filename='aoc 2018 d5 input.txt'

for line in open(filename):
	code=line

limit =len(code)
code2=code
i=0
count=0
while i < (limit-count):
	if code[i].casefold()==code[i+1].casefold() and ((code[i].isupper() and code [i+1].islower()) or (code[i+1].isupper() and code [i].islower())):
		code = code[:i]+code[i+2:]
		i-=2
		count=limit-len(code)
	i+=1
	if i==-1:
		i+=1
	answer1=len(code)
	count=limit-len(code)+1
	
print ('The deconstructed length of the polymer is ', answer1)
#~~~~~~~~~ part 2
alphabet='abcdefghijklmnopqrstuvwxyz'
lenalph=len(alphabet)

j=0
answer2=50000
answer2b=0
for j in range(lenalph):
	i=0
	code=code2
	code=code.replace(alphabet[j],"")
	code=code.replace(alphabet[j].capitalize(),"")
	while i < (limit-count):
		if code[i].casefold()==code[i+1].casefold() and ((code[i].isupper() and code [i+1].islower()) or (code[i+1].isupper() and code [i].islower())):
			code = code[:i]+code[i+2:]
			i-=2
			count=limit-len(code)
		i+=1
		if i==-1:
			i+=1
		answer2b=len(code)
		count=limit-len(code)+1
	if answer2b < answer2:
		answer2 = answer2b
	
print("The min length without bad apple letter is", answer2)
