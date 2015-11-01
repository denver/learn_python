# testresults.py

from scorelibrary import scorelib

# This should be a 'Module' to define the possible scoring rolls

def straight(self):
	if self == ({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}):
		print "A straight!"
		print "You scored %s" %  (scorelib["straight"])

def sixofakind(self):
	for k, v in sorted(self.items()):
		if v == 6:
			print "6 of a kind!"
			print "You scored %s" %  (scorelib["sixofakind"])

def fiveofakind(self):
	for k, v in sorted(self.items()):
		if v == 5:
			print "5 of a kind!"
		# print k,v

def fourofakind(self):
	for k, v in sorted(self.items()):
		if v == 4:
			print "4 of a kind!"
		# print k,v

def threeofakind(self):
	triples = 0
	triplekey = []
	for k, v in sorted(self.items()):
		if v == 3:
			triples += 1
			triplekey.append(k)

	# checks if there are two or one set of threes - if two it's a special roll 
	if triples == 2:
		print "Two triples"
		print scorelib['twotriple']
	elif triples == 1:
		print "Three %ss" % (triplekey[0])
		if triplekey[0] == 1:
			print "You scored 300"
		else:
			print "You scored %s" % (triplekey[0] * 100)

def threepairs(self):
	totalpairs = 0
	for k, v in sorted(self.items()):
		if v == 2:
			totalpairs += 1
	if totalpairs == 3:
		print "Three pairs"
		print scorelib['threepairs']

def printpairs(self):
	for k, v in sorted(self.items()):
		print k,v

