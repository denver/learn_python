# scoreroll.py by dp 10.31.15

# Create Class to Score the Roll of the Dice 

class Score(object):
	def __init__(self, roll):
		self.roll = roll

	def theroll(self):
		print self.roll
		for i in self.roll:
			print "You rolled %s %ss" % (self.roll[i], i)

	# def straight(self):
	# 	if self.roll == {1:1,2:1,3:1,4:1,5:1,6:1}:
	# 		print "you rolled a straight!"

	def sixofakind(self):
		if self.roll == {1:0,2:0,3:0,4:0,5:0,6:6}:
			print "six of a kind!"


	# def specialrolls(self):
	# 	checkers = self.roll
	# 	if checkers.straight():
	# 		print "the special straight!"
	# 	elif checkers.sixofakind():
	# 		print "six special of a kind"



# print example
# # example.theroll()

# example.straight()
# example.sixofakind()


