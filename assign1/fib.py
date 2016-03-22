import sys
#Leonardo Matos
#How to use: call this program passing one number as parameter

#Function fib recieves a number and calculates it's fibonacci value recursivelly
def fib(x):
	if x == 0:
            return 0
	elif x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)

try:    
    x = int(sys.argv[1])
    print fib(x)
    
except ValueError:
    print 'Only numbers are accepted as parameters'
    
except IndexError:
    print 'This program requires one number as parameter'