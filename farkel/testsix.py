# testsix.py

import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual

sixofakind = False
total_rolls = 0

while sixofakind == False:
	total_rolls += 1
	a = roll(6)
	#print a
	sixofakind = checkEqual(a)

print a
print "It took %s rolls to get six of a kind! 3000pts!" % (total_rolls)