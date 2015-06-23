# Example 14

from sys import argv

script, user_name, computer_name = argv
prompt = '='

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "do you like me %s?" % user_name
likes = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer named %r. Nice.
""" % (likes, lives, computer, computer_name)


# I loved Zork! I played it as a kid - Which probably explains why I'm into this shit. 
# http://thcnet.net/zork/index.php

# I also liked the Choose Your own Adventure Series of books though I'm not stopping to learn more about it. I get it.
