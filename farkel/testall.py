# testall.py

from roll import Roll
from score import Score
from turn import Turn

dice = 6

#d = {1: 0, 2: 3, 3: 1, 4: 0, 5: 0, 6: 2}   # farkel condition object 

a = Roll(dice)
b = a.roll()
c = Score(b)

c.theroll()
c.straight()
c.sixofakind()
c.fiveofakind()
c.fourofakind()
c.threeofakind()
c.threepairs()

