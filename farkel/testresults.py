# testresults.py

from scorelibrary import scorelib

# This should be a 'Module' to define the possible scoring rolls

def straight(self):
	if self == ({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}):
		print "fuck yeah! a straight!"

def sixofakind(self):
	if self == ({1: 6, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}):
		print "fuck yeah! six of a kind!"
	# for a in self:
	# 	if a[b[i]] == 6: # a[b[i]] += 1
	# 		print "fuck yeah! six of a kind"