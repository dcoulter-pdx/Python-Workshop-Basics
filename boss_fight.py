#BOSS FIGHT
from math import *

def Discriminant(a,b,c):
	d = pow(b,2) - 4*a*c
	if d < 0:
		return -1
	elif d == 0:
		return 0
	else:
		return 1

def Roots(a,b,c):

	d = Discriminant(a,b,c) 

	if d < 0:
		return "Why you so complex?"
	elif d == 0:
		single = -b / (2*a)
		return "One root, multiplicity 2 at: %r" % single
	else:
		plus = (-b + sqrt(pow(b,2) - 4*a*c))/(2*a)
		minus = (-b - sqrt(pow(b,2) - 4*a*c))/(2*a)
		return "Plus root: %r, Minus root: %r" % (plus,minus)


print """
Welcome to your DOOM, where we happily find the roots
any 2nd degree polynomial that you wish.

Proceed with caution!
"""

prompt = "> "
a = 0.0
b = 0.0
c = 0.0

while (a == 0.0):
	print "Co-efficient of x^2:"
	a = float(raw_input(prompt))

print "\nSplendid!\n"

while (b == 0.0):
	print "Co-efficient of x:"
	b = float(raw_input(prompt))

print "\nMarvelous!\n"

while (c == 0.0):
	print "Constant term:"
	c = float(raw_input(prompt))

print "\nBrilliant! Crunching ...\n"

print "Message for you sir:\n%s\n" % Roots(a,b,c)

