# farkel python simulator
# Class List for all major first rolls 
# generate random integers for test purposes

import random 
from urllib import urlopen
import sys

# create a container dict for current roll
current_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

# create a container dict for scored rolls (i.e. to be counted if no farkel and to determine 6-n for next roll )
score_roll = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

total_score = 0
round_score = 0

