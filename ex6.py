# Get some!
from math import *


def Print_A_Joke():
	print "\nWhat is the contour integral around Western Europe?\nZero!"\
	" All the Poles are in Eastern Europe!\n"

def Pythagorean(x,y):
	return sqrt(pow(x,2) + pow(y,2))

def Variable_Length_HooHaw(*args):
	for i in xrange(len(args)):
		print "%i arg: %r" % (i, args[i])
	print ""


Print_A_Joke()

x = 3
y = 4
print "A triangle with perpendicular side lengths "\
	  "%d and %d has a hypotenuese of %d\n" % (x,y,Pythagorean(x,y))

Variable_Length_HooHaw('1', 2, True, sin(3*pi/2))