# roll.py
# generate random integers for test purposes

import random 
from urllib import urlopen
import sys

def roll(diceleft):
	myroll = []
	for x in range(0, diceleft):
		a = random.randint(1, 6)
	 	myroll.append(a)
	return myroll

