import numpy as np

inputarray=np.empty(((1000,1000)))

#1 @ 604,100: 17x27
for line in open('AoC 2018 D3 input.txt'):
	coordinates = line.split()
	i,j=coordinates[2].split(',')
	i,j=int(i),int(j[:-1])
	w,h=coordinates[3].split('x')
	w,h=int(w),int(h)
	for dx in range(w):
		for dy in range(h):
			inputarray[(i+dx),(j+dy)]+=1
	
answer=0
krange=inputarray.shape[0]
lrange=inputarray.shape[1]
for k in range (krange):
	for l in range(lrange):
		if inputarray[k,l]>1:
			answer+=1
		
print ("total square inches of overlap is ", answer)

for line in open('AoC 2018 D3 input.txt'):
	coordinates = line.split()
	i,j=coordinates[2].split(',')
	i,j=int(i),int(j[:-1])
	w,h=coordinates[3].split('x')
	w,h=int(w),int(h)
	testarray=np.empty((w,h))
	for dx in range(w):
		for dy in range (h):
			testarray[dx,dy]=inputarray[(i+dx),(j+dy)]
	clearedarray=testarray-np.ones((w,h))	
	if clearedarray.sum() == 0:
		answer2=coordinates[0]
	
print ("the only claim with no overlap is ", answer2)