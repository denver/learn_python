# farkel python simulator

import random 
from urllib import urlopen
import sys

# python farkel game 
# author : Denver Peterson
# last update 10.28.2015

def roll(diceleft):
	myroll = []
	for x in range(0, diceleft):
		a = random.randint(1, 6)
	 	myroll.append(a)
	return myroll



