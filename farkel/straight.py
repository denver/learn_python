#straight.py 

import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual

isstraight = False
total_rolls = 0

while isstraight == False:
	total_rolls += 1
	a = roll(6)
	print a
	a.sort();
	#print a
	if a == [1,2,3,4,5,6]:
		isstraight = True
	#straight = checkEqual(a)

print a
print "It took %s rolls to roll a straight! 1500pts!" % (total_rolls)