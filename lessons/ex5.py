name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 # inches
weight = 180.00 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

convert_lb_kg = weight * .453592
convert_in_cm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." %  height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tring, try to gte it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight
	, age + height + weight)

print "My height in cm is %f." % convert_in_cm
print "My weight in kg is %f." % convert_lb_kg