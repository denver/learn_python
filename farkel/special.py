
from roll import Roll
from score import Score
from turn import Turn
import random 
import sys

# class Special(object):

# 	def __init__(self, roll):
# 		self.roll = roll

def checkspecial(self):
	self.roll = self
		
	self.roll.straight()
	self.roll.sixofakind()
	self.roll.fiveofakind()
	self.roll.fourofakind()
	self.roll.threeofakind()
	self.roll.threepairs()
