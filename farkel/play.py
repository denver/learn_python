# play.py

from farkel import roll, checkEqual, sortroll, addscore, roll_dice
from scorelibrary import scorelib
from testresults import straight

#result = [1,2,3,4,5,6]
result = roll(6)

print result 

c = sortroll(result)

print c

#print scorelib['one']

foo = straight(c)