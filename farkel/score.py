# farkel python simulator
# Class List for all major first rolls 
# generate random integers for test purposes

from collections import defaultdict
import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual
from scoreroll import Score

# create a container dict for current roll
current_roll = {1:0,2:0,3:0,4:0,5:0,6:0}

# # create a container dict for scored rolls (i.e. to be counted if no farkel and to determine 6-n for next roll )
score_roll = {1:0,2:0,3:0,4:0,5:0,6:0}

total_score = 0
round_score = 0

# print "current roll = %s" % (current_roll)

# print "score roll = %s" % (score_roll)

b = roll(6)

a = {1:0,2:0,3:0,4:0,5:0,6:0}

# Have analyze why this doesn't work 

# for item in b:
# 	#a[b[item]] = a[b[item]] + 1
# 	print item
# 	#print [b[item]]

# for n in b:
#    a[b[n]] += 1

print "You rolled %s " % b

for i in range(len(b)):
	#print a[b[i]] + 1
	a[b[i]] += 1
	#print "the index is %s and the dice value is %s" % (i,b[i])
	#print b[i]
	#print "adding +1 to %ss column" % b[i]
	
	#print a

print a


# c = Score(b)
# c.theroll()





