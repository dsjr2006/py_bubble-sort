# Bubble Sort - Darwin Smith II - 2015-9-9
import random, datetime
theList = []
number = 100
start = 0
stop = 0
#Populate list with 100 random values 1-1000
while number > 0:
	theList.append(random.randint(1, 1000))
	number -= 1

print 'Before:', theList ,'\n\n'	

for numerals in range(len(theList)-1,0,-1):
	if start == 0:
		start = datetime.datetime.now()
        for i in range(numerals):
            if theList[i]>theList[i+1]:
                theList[i],theList[i+1]=theList[i+1],theList[i] 
stop =  datetime.datetime.now()
print 'After:', theList
print '\nArrange Time:', (stop - start)