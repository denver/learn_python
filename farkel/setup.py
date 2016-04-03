# setup.py
# Game setup 

print "Welcome to Farkel"
print "A game of Guts and Luck\n"

def players():
	numPlayers = raw_input("How many players? ")
	if numPlayers.isnumeric() == True:
		print("There are %r players ") % (numPlayers)
	else:
		print("Please enter the number of players")



players()

