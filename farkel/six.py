#six.py
# random.py
# generate random integers for test purposes
import random 
from urllib import urlopen
import sys

# set variable to print at the end, maintain count
#total_rolls = 0
# set diceleft
diceleft = 112
#blah = []

elements = []
#a = []

# commented out, easy "hack" of creating first array of six rolls 
# roll = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]

# function to check if all items in the roll are equal
def checkEqual(lst):
       return lst[1:] == lst[:-1]

# function to roll remaing dice in cup n = 1-6
def roll():
	result = []
	total_rolls = 0
	#a = []
	for x in range(0, diceleft):
		total_rolls = total_rolls + 1
		roll = random.randint(1, 6)
		print roll
		#result = result.append(1)
		#a = a.append(roll)
		#a = a.append(x)
		#print a
		print "Total rolls > %r" % (total_rolls)

# write a test 
test_var = [ 1, 1, 1, 1, 1, 1,]
print "Did your test pass? > %r" % (checkEqual(test_var))


# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)


roll()
