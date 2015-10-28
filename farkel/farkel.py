# farkel python simulator

import random 
from urllib import urlopen
import sys

# python farkel game 

# create global variable for the roll

container = []

# def roll(dice):
# 	for i in range()
# 	return radom.randint(1,6)

def checkEqual1(iterator):
      try:
         iterator = iter(iterator)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True



