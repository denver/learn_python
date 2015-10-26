#six.py
# random.py
# generate random integers for test purposes
import random 
from urllib import urlopen
import sys

i = False
total_rolls = 0
# roll = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
diceleft = 6

# print "You rolled %s" % (roll)

#for i in diceleft:
#	print "you rolled > %s" % (roll)

while i is False:
	roll = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
    print "You rolled %s" % (roll)
    total_rolls = total_rolls + 1
    i = True

    
    


