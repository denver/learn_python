# six.py

import random 
from urllib import urlopen
import sys

# set variable to print at the end, maintain count

# set diceleft - will determine amount of dice rolled
diceleft = 6
#set myroll
#myroll = []

#a = []

# commented out, easy "hack" of creating first array of six rolls 
# roll = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]

# function to check if all items in the roll are equal
def checkEqual(lst):
       return lst[1:] == lst[:-1]

# function to roll dice n = 1-6 dice
def roll():
	total_rolls = 0
	myroll = []
	for x in range(0, diceleft):
		total_rolls = total_rolls + 1
		a = random.randint(1, 6)
		#print a 
	 	myroll.append(a)
		#print myroll
		#print "Total rolls > %r" % (total_rolls)
	print myroll

# write a test 
# test_var = [ 1, 1, 1, 1, 1, 1,]
# print "Did your test pass? > %r" % (checkEqual(test_var))

roll()


