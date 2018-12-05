import numpy as np
from datetime import datetime as dt

filename='aoc 2018 d5 input.txt'

for line in open(filename):
	code=line

limit =len(code)

i=0
count=0
while i < (limit-count):
	if code[i].capitalize()==code[i+1].capitalize() and ((code[i].isupper() and code [i+1].islower()) or (code[i+1].isupper() and code [i].islower())):
		code = code[:i]+code[i+2:]
		i-=2
		count=limit-len(code)
	i+=1
	answer1=len(code)
	count=limit-len(code)+1
	
print ('The deconstructed length of the polymer is ', answer1)