import sys
#Leonardo Matos
#How to use: Call this program passing three number as parameters

#Function fibit recieves number as parameters and calculates it's value recursivelly.

def fibit(x,a,b):
	if x == 0:
            return a
	elif x == 1:
            return b
        else:
            return fibit(x-1,b,a+b)

try:    
    x = int(sys.argv[1])
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print fibit(x,a,b)
    
except ValueError:
    print 'Only numbers are accepted as parameters'
    
except IndexError:
    print 'This program requires three number as parameter'