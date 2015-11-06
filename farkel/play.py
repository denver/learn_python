# play.py

from farkel import roll, checkEqual, sortroll, addscore, roll_dice
from scorelibrary import scorelib
from testresults import straight, sixofakind, fiveofakind, fourofakind, threeofakind, threepairs, printpairs
from scoreroll import Score

result = [1,1,1,1,1,1]
#result = roll(6)

print result 

c = sortroll(result)

# print c

# printpairs(c)

# straight(c)
# sixofakind(c)
# fiveofakind(c)
# fourofakind(c)
# threeofakind(c)
# threepairs(c)



somevar = Score(c)

somevar.theroll()
somevar.sixofakind()



