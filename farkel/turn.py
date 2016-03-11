# turn.py
# module to encompass a players turn

from roll import Roll

class Turn(object):

	def __init__(self, player):
		self.player = player

	def turn(self):
		# rollagain = False
		print "It's %ss turn" % self.player
		print "%s rolled:" % self.player 
		# a = Roll(6)
		# b = a.roll()
		# print b
		# #b.theroll()
		#print b







