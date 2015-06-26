#ex33.py
#i = 0




numbers = []
end = raw_input("> ")

def gotcha(end):
	i = 0
	while i < end: 
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

gotcha(end)

print "The numbers: "

for num in numbers:
	print num


