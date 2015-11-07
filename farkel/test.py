# test.py
# this test file to test creating logic for 
#import random 
# from farkel import roll, checkEqual, sortroll, addscore, roll_dice
# from scorelibrary import scorelib
#from testresults import straight, sixofakind, fiveofakind, fourofakind, printpairs, threeofakind, threepairs
# from scoreroll import Score
from roll import Roll
from turn import Turn

# #result = [1,1,1,2,1,2]
# result = roll(6)
# print result 

# c = sortroll(result)
# print c

# printpairs(c)

# straight(c)
# sixofakind(c)
# fiveofakind(c)
# fourofakind(c)
# threepairs(c)
# threeofakind(c)

# somevar = Score(c)
# print somevar 

# somevar.straight()
# somevar.sixofakind()
# somevar.fiveofakind()
# somevar.fourofakind()
# somevar.threeofakind()
# somevar.threepairs()
# somevar.printpairs()
# somevar.theroll()
player = "Denver"
n = 2
result = Roll(n)
 
somevar = result.roll()
print somevar
# somevar2 = somevar.sortroll()
# print somevar2

x = Turn(player)

x.turn()




