# garbage.py

# a dumping ground for WIP or dead and dying code for this project
# ie. working ugly functions and first attempts at creating the rolls, iterations and scoring. 
# here for posterity and learning purposes only, also to keep in case the other files get complex and I can't get it working.


# How Fajar helped me learn to increase a value of the key : value pair in a dict
# it's getting the value of a at b index and iterating (adding 1 to the value)

# final choice for iterating over list
# a[b[i]] += 1

#a[b[i]] = a[b[i]] + 1   # This adds 1 to the 'value' of the 'key' 

# a[b[0]] = a[b[0]] + 1
# a[b[1]] = a[b[1]] + 1
# a[b[2]] = a[b[2]] + 1
# a[b[3]] = a[b[3]] + 1
# a[b[4]] = a[b[4]] + 1
# a[b[5]] = a[b[5]] + 1

# Have analyze why this doesn't work - can problaby ditch this crap

# for item in b:
# 	#a[b[item]] = a[b[item]] + 1
# 	print item
# 	#print [b[item]]

# for n in b:
#    a[b[n]] += 1

# stuff related to running the classes which I broke

# a = roll(6)
# # a = [1,2,3,4,5,6]
# # a = {1:0,2:0,3:0,4:0,5:0,6:6}
# test = Score(a)

# # newroll = roll(6)
# print a

# # a = sortroll(a)
# # # blah = Score(a)
# print test 
# test.theroll()
# test.sixofakind()
# test.straight()


# print scorelib['one']


# # first attempt at three pair check 

# def threepairs(self):
# 	totalpairs = 0
# 	for k, v in sorted(self.items()):
# 		if v == 2:
# 			totalpairs += 1
# 			# print "you have two %ss" % k
# 			# print "you rolled %s pairs" % totalpairs
# 	if totalpairs == 3:
# 		print "you rolled three pairs"
# 		print scorelib['threepairs']




# def fourofakind(self):
# 	ispair = 0
# 	for k, v in sorted(self.items()):
# 		if v == 4:
# 			for k, v in sorted(self.items()):
# 				if v ==2:
# 					ispair +=1
# 					print "4 of a kind and a pair!"

# 			if ispair == 0:
# 				print "4 of a kind!"
# 		# print k,v

# def fourofakind(self):
# 	for k, v in sorted(self.items()):
# 		if v == 4:
# 			for k, v in sorted(self.items()):
# 				if v !=2:
# 					#print v
# 					print "4 of a kind!"
# 		# print k,v


# fourofakind(c)



# python farkel game 
# author : Denver Peterson
# last update 11.1.2015

# import random 
# from urllib import urlopen
# import sys
# from scoreroll import Score


# def checkEqual(self):
#        return self[1:] == self[:-1]

# def roll(diceleft):
# 	myroll = []
# 	for x in range(0, diceleft):
# 		a = random.randint(1, 6)
# 	 	myroll.append(a)
# 	return myroll

# def sortroll(rollofdice):
# 	a = {1:0,2:0,3:0,4:0,5:0,6:0}
# 	for i in range(len(rollofdice)):
# 	#print a[b[i]] + 1
# 		a[rollofdice[i]] += 1
# 		#print "the index is %s and the dice value is %s" % (i,b[i])
# 		#print b[i]
# 		#print "adding +1 to %ss column" % b[i]
# 		#print a
# 	return a

# def addscore(userscore):
# 	totalscore = roundscore + totalscore
# 	return totalscore

# def roll_dice(self):
# 	return roll(self)

