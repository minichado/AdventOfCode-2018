import numpy as np
from datetime import datetime as dt
from datetime import timedelta,date, time

#this is currently not working, issues parsing the times, currently missing 
#a timeslot as well as some time shifts in the output.  preserving
#in case I finish this later

filename='aoc 2018 d4 input sample.txt'
#sample input line
#[1518-09-20 00:43] falls asleep

#counting total rows in input so
#i can initialize an array of the correct size

rows=0
for line in open(filename):
	rows+=1
	
#initializing array to hold input
#just learned that NumPy arrays default to numbers, 
#forceing dtype=object to hold strings
fulllist=np.zeros((rows),dtype=object)
i=0
for line in open(filename):
	text=line[19:].replace("\n","")
	dataline=line.split()
	h,min=dataline[1].split(":")
	h,min=int(h),int(min[:-1])
	parseddate=line[:17].replace("[","")
	date2=dt.strptime(parseddate, '%Y-%m-%d %H:%M')
	fulllist[(i)]=(date2,h,min,text)
	i+=1
		
#sorting array by date/time	
sorted=np.sort(fulllist)
#now that it's sorted, I'm going to tack guard ID on the front of each shift
guarded=np.zeros((rows),dtype=object)
#print(sorted[0])
j=0
for j in range(rows):
	dataline=sorted[j][3].split()
	isguard=dataline[1][1:]
	if isguard.isdigit():
		guarded[(j)]=(int(isguard),sorted[j][0],sorted[j][1],sorted[j][2],sorted[j][3].split()[0])
	else:
		guarded[(j)]=(guarded[j-1][0],sorted[j][0],sorted[j][1],sorted[j][2],sorted[j][3].split()[0])

print(guarded[5][1].date(),guarded[5][2])

#at this point I have every action in order, and the guarded
#array has each row starting with the attributed guard

#I think I'm going to make an array to count how much each guard naps and go from there
#guarded format
#<guardnumber,date,hour,minute,action>

sleeping=np.zeros((rows,60+1),dtype=object)
sleeprow=rowsrange=m=0
for k in range(rows-1):
	l=0
	
	if guarded[k][1].date()==guarded[k+1][1].date() and guarded[k][0]==guarded[k+1][0]:
		rowsrange+=1
	else:
		sleeping[(sleeprow,0)]=guarded[k-rowsrange][0]
		sleeping[(sleeprow,1)]=guarded[k-rowsrange][1]
		#print(guarded[k-rowsrange][0])
		m=0
		for l in range(60):
			for m in range(rowsrange+2):
				if guarded[k-rowsrange+m-1][4]=='Guard':
					while l<guarded[k-rowsrange+m][3]:
						#print ('guard',k,l,m,rowsrange,sleeprow)
						sleeping[(sleeprow,l+2)]=0
						l+=1
				elif guarded[k-rowsrange+m-1][4]=='falls':
					while l<guarded[k-rowsrange+m][3]:
						sleeping[(sleeprow,l+2)]=1
						#print ('falls',k,l,m,rowsrange,sleeprow)
						l+=1
				elif guarded[k-rowsrange+m-1][4]=='wakes':
					while l<guarded[k-rowsrange+m][3]:
						sleeping[(sleeprow,l+2)]=0
						#print ('wakes',k,l,m,rowsrange,sleeprow)
						l+=1
			m+=1
			l+=1

		sleeprow+=1

		rowsrange=0
print(sleeping[0:5])
print(guarded[1][3])

#tbd
#sum rows elemens 1:61
#add sum for all matching elements 0
#after identifying largest sleeper, find highest occurence of sleepe
#add all rows to themselves, look for max value in row, pull out column, done
