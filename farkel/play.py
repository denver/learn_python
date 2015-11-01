# play.py

from farkel import roll, checkEqual, sortroll, addscore, roll_dice
from scorelibrary import scorelib
from testresults import straight, sixofakind


#result = [1,1,1,1,1,1]
result = roll(6)

print result 

c = sortroll(result)

print c

#print scorelib['one']

straight(c)
sixofakind(c)
