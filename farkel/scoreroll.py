# scoreroll.py by dp 10.31.15

# Create Class to Score the Roll of the Dice 

class Score(object):
	def __init__(self, roll):
		self.roll = roll

	def theroll(self):
		print self.roll
		for i in self.roll:
			print "You rolled %s %ss" % (self.roll[i], i)

# print example
# # example.theroll()

# example.straight()
# example.sixofakind()


