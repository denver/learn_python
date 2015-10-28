# ex_periment.py

import random

min = 1
max = 6

roll_again = False
total_rolls = 0

def checkEqual(lst):
       return lst[1:] == lst[:-1]

while roll_again == False:
	total_rolls = total_rolls +1
	b = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
	print b
	roll_again = checkEqual(b)

print "It took %s rolls to get six of a kind! 3000pts!" % (total_rolls)