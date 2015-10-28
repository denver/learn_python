#six.py
# random.py
# generate random integers for test purposes
import random 
from urllib import urlopen
import sys

# set variable to print at the end, maintain count
#total_rolls = 0
# set diceleft
diceleft = 6
#blah = []

# commented out, easy "hack" of creating first array of six rolls 
# roll = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]

# function to check if all items in the roll are equal
def checkEqual(lst):
       return lst[1:] == lst[:-1]

# function to roll remaing dice in cup n = 1-6
def roll():
	result = [0]
	total_rolls = 0
	a = []
	for x in range(0, diceleft):
		total_rolls = total_rolls + 1
		roll = random.randint(1, 6)
		print roll
		#result = result.append(1)
		#a = a.append(roll)
		print a
		print "Total rolls > %r" % (total_rolls)

# write a test 
# test_var = [ 1, 1, 1, 1, 1, 1,]
# print checkEqual(test_var)

roll()
