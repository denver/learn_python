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