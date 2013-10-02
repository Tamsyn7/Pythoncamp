import sys
number =(int) (sys.argv[1])

#if number % 2 == 0: 
#    print 'even'
#else 
#    print 'odd'
    
if (number < 50) and (number> 0):
    print "Minor"
if (number <1000):
    print "Major"
else:
    print "Severe"
