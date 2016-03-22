import sys

def fibPow (n,a,b):
    #define identity matrix
    identity={}
    identity[0,0]=1
    identity[0,1]=1
    identity[1,0]=1
    identity[1,1]=0
    
    #Define the L matrix according to supplied values
    L={}
    L[0,0]= a+b
    L[0,1]= b
    L[1,0]= b
    L[1,1]= a
    
    #Base cases
    if (n == 0):
        return 0
    if (n == 1):
        return 1
               
    #Exponentiation implementation 
    for x in range(1,n-1):
        a = (L[0,0]*identity[0,0])+(L[0,1]*identity[1,0])
        b = (L[0,0]*identity[0,1])+(L[0,1]*identity[1,1])
        c = (L[1,0]*identity[0,0])+(L[1,1]*identity[1,0])
        d = (L[1,0]*identity[0,1])+(L[1,1]*identity[1,1])
        L[0,0] = a
        L[0,1] = b
        L[1,0] = c
        L[1,1] = d
        
    #result
    return L[0,0]
    
try:    
    x = int(sys.argv[1])
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print fibPow(x,a,b)
    
except ValueError:
    print 'Only numbers are accepted as parameters'
    
except IndexError:
    print 'This program requires three numbers as parameters'

#Expected results
#0  1   2   3   4   5   6
#0  1   1   2   3   5   8