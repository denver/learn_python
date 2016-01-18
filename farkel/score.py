# score.py

from scorelibrary import scorelib
#from roll import Roll
#from turn import Turn

class Score(object):
	
	def __init__(self, roll):
		self.roll = roll

	def straight(self):
		if self.roll == ({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}):
			print "A straight!"
			print "You scored %s" % (scorelib["straight"])

	def sixofakind(self):
		for i in self.roll:
			if self.roll[i] == 6:
				print "6 of a kind!"
				print "You scored %s" % (scorelib["sixofakind"])

	def fiveofakind(self):
		for i in self.roll:
			if self.roll[i] == 5:
				print "5 of a kind!"
				print "You scored %s" % (scorelib["fiveofakind"])

	def fourofakind(self):
		ispair = 0
		for k, v in sorted(self.roll.items()):
			if v == 4:
				for k, v in sorted(self.roll.items()):
					if v ==2:
						ispair +=1
						print "4 of a kind and a pair!"
						print "You scored %s" % (scorelib["fourofakindpair"])

				if ispair == 0:
					print "4 of a kind!"
					print "You scored %s" % (scorelib["fourofakind"])

	def threeofakind(self):
		triples = 0
		triplekey = []
		for k, v in sorted(self.roll.items()):
			if v == 3:
				triples += 1
				triplekey.append(k)

		# checks if there are two or one set of threes - if two it's a special roll 
		if triples == 2:
			print "Two triples"
			print "You scored %s" % (scorelib["twotriple"])
		elif triples == 1:
			print "Three %ss" % (triplekey[0])
			if triplekey[0] == 1:
				print "You scored 300"
			else:
				print "You scored %s" % (triplekey[0] * 100)

	def threepairs(self):
		totalpairs = 0
		for k, v in sorted(self.roll.items()):
			if v == 2:
				totalpairs += 1
		if totalpairs == 3:
			print "Three pairs"
			print scorelib['threepairs']

	def theroll(self):
		print self.roll
		for i in self.roll:
			print "You rolled %s %ss" % (self.roll[i], i)

	

