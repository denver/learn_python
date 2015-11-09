#bigdata.py

import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual

sixofakinds = 0
total_rolls = 0
sixofakind = False

for x in range (0, 1000000):
	total_rolls += 1
	a = roll(6)
	#print a
	if checkEqual(a) == True:
		sixofakinds += 1

print "There were %s Six of a Kind rolls in %s rolls! 3000pts!" % (sixofakinds, total_rolls)