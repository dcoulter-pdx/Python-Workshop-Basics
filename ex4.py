print "Ifs, elifs, and elses Oh My!"

# Basic if-else
# Note the whitespace - it creates "scope"
if (1 == 1):
	print "Math works"
else:
	print "The world is shit."

# Deluxe if-else

if ("hello" == "hello" and False):
	print """
	The way is shut.
	It was made by those who are Dead,
	and the Dead keep it,
	until the time comes.
	The way is shut.
	"""
elif (1 + 1) == 2:
	print "Whew! Glad we got outta there!"
else:
	print "Apparently we're now in Moria."

# Your garden variety for-loop. 
for i in xrange(1,10):

	print "index = %d" % i

# A charming, and avuncular while-loop
bobsYourUncle = False
while not bobsYourUncle:

	i -= 1

	if i == 1:
		bobsYourUncle = True

print "Apparently Bob is now your uncle."
