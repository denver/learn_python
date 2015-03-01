# example 15
# imports the argument value module
from sys import argv
#take the value of the script and the file into the argument value as variables
script, filename = argv 
#makes a variable called txt out of the openting of the file given in the cmd line as argv
txt = open(filename)
# prints out the text saying which file will be open
print "Here's you file %r:" % filename
# prints the output of the file you passed in the cmd line
print txt.read()
#another print out asking for the same or different file name
print "Type the filename again:"
#prompts user for the new file
file_again = raw_input("> ")
#assigns the variable txt again to the opening of the file given above
txt_again = open(file_again)
#prints the output of the file
print txt_again.read()

#new line to commit
