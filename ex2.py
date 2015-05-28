print "\nTime to do some math\n"

gin = 100
tonic = 120
physicists = 15

print "There are %d gins, %d tonics, and %d physicists\n"\
% (gin, tonic, physicists)

diff = tonic - gin

print "That means we have %d more tonics than we need!" % diff

print """
How many G&Ts does each physicist fairly get?
"""

fair_share = gin / 15

print "%d of course" % fair_share

left_overs = gin - (fair_share * physicists)

print """
That leaves %d left over!
""" % left_overs

print "The engineers can squabble over the left over %d G & Ts\n"\
% left_overs