#example 17
#imports the argv value
from sys import argv
#I don't know what this does yet. 
from os.path import exists
# takes the script name, and two input variables. 
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do thse two on one line, how?
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hi RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

