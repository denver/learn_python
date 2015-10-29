# farkel python simulator
# Class List for all major first rolls 
# generate random integers for test purposes
from collections import defaultdict
import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual

# create a container dict for current roll
current_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

# create a container dict for scored rolls (i.e. to be counted if no farkel and to determine 6-n for next roll )
score_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

total_score = 0
round_score = 0


# print "current roll = %s" % (current_roll)

print "score roll = %s" % (score_roll)

print roll(6)


# https://docs.python.org/2/tutorial/datastructures.html