# turn.py
# module to encompass a players turn

class Turn(object):
	def __init__(self, player):
		self.player = player

	def turn(self):
		print "It's %ss turn" % self.player