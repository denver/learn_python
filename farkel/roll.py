# roll.py
# generate dice roll returns a dict with key:value pairs 

import random 
import sys

class Roll(object):
	
	def __init__(self, dice):
		self.dice = dice

	def roll(self):
		a = {1:0,2:0,3:0,4:0,5:0,6:0}
		self.roll = []
		for i in range(0, self.dice):
			self.roll.append(random.randint(1, 6))
		for i in range(len(self.roll)):
			a[self.roll[i]] += 1
		return a