# python farkel game 
# author : Denver Peterson
# last update 11.1.2015

import random 
from urllib import urlopen
import sys
from scoreroll import Score


def checkEqual(self):
       return self[1:] == self[:-1]

def roll(diceleft):
	myroll = []
	for x in range(0, diceleft):
		a = random.randint(1, 6)
	 	myroll.append(a)
	return myroll

def sortroll(rollofdice):
	a = {1:0,2:0,3:0,4:0,5:0,6:0}
	for i in range(len(rollofdice)):
	#print a[b[i]] + 1
		a[rollofdice[i]] += 1
		#print "the index is %s and the dice value is %s" % (i,b[i])
		#print b[i]
		#print "adding +1 to %ss column" % b[i]
		#print a
	return a

def addscore(userscore):
	totalscore = roundscore + totalscore
	return totalscore

def roll_dice(self):
	return roll(self)



