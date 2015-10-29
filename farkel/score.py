# farkel python simulator
# Class List for all major first rolls 
# generate random integers for test purposes
from collections import defaultdict
import random 
from urllib import urlopen
import sys
from farkel import roll, checkEqual

# create a container dict for current roll
# current_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

# # create a container dict for scored rolls (i.e. to be counted if no farkel and to determine 6-n for next roll )
# score_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

# total_score = 0
# round_score = 0


# # print "current roll = %s" % (current_roll)

# print "score roll = %s" % (score_roll)

b = roll(6)
print b 

# https://docs.python.org/2/tutorial/datastructures.html

a = {1:0,2:0,3:0,4:0,5:0,6:0}
#b = [2, 2, 5, 5, 5, 3]
for index in b:
   a[b[index]] += 1

print a



# >>> a
# {'1': 0, '2': 0}
# >>> b
# [1, 1]
# >>> a['1']
# 0
# >>> b
# [1, 1]
# >>> a
# {'1': 0, '2': 0}
# >>> a[0] = b[0]
# >>> a
# {'1': 0, 0: 1, '2': 0}
# >>> a = {"1" : 0 , "2" : 0}
# >>> a
# {'1': 0, '2': 0}
# >>> a[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 0
# >>> a['1'] = b[0]
# >>> a
# {'1': 1, '2': 0}
# >>> a = {"1" : 0 , "2" : 0}
# >>> b
# [1, 1]
# >>> a = {1 : 0 , 2 : 0}
# >>> a
# {1: 0, 2: 0}
# >>> a[b[0]] = a[b[0]] + 1
# >>> a
# {1: 1, 2: 0}
# >>> a[b[1]] = a[b[1]] + 1
# >>> a
# {1: 2, 2: 0}
# >>> ++a[b[0]]
# 2
# >>> a
# {1: 2, 2: 0}
# >>> a[b[0]] += a[b[0]]
# >>> a
# {1: 4, 2: 0}
# >>> a[b[0]] += a[b[0]]
# >>> a[b[0]] += 1
# >>> a
# {1: 9, 2: 0}
# >>> a[b[0]] += 1
# >>> a
# {1: 10, 2: 0}
# >>>