import sys,argparse
#Test
#3 10a 11 19 20 21b 32b 39 41 39

def sortedHasSum (s, n):
    if (len(s) < 2):
        return False
    a = 0       #Pointer going left to right
    b = len(s)  #Pointer going right to left
    rest = 0    #what the currently selected number is missing to match n
    
    #Basically the pointers go towards the center of the list
    #looking for the number they need, if the number they need is 
    #not in the array they choose a new needed number or 'rest'        
    while a < b:
        rest = n-int(s[a])  #Choose a new needed number or rest according to a
        b = b - 1

        while (s[b] >= rest):
            if (a >= b):
                return False #The pointers met, not sum equals n
            if s[b] == rest:
                return str(True)+': '+str(s[a])+" & "+str(s[b])
            b = b-1

        rest = n-s[b] #Choose a new needed number or rest according to b 
        a = a + 1
        while (s[a]<= rest):
            if (a >= b):
                return False #The pointers met, not sum equals n
            if s[a] == rest:
                return str(True)+': '+str(s[a])+" & "+str(s[b])
            a = a + 1
   
   
########################################
########################################
#Define a parser
parser = argparse.ArgumentParser(description='Find if two number in a list is equal to the last suplied number in the list.')
parser.add_argument('--list', metavar='N', type=int, nargs='+',
                   help='a list of integers') 

#Read args
try:    
    args = parser.parse_args()
    if (len(sys.argv) < 2):
        raise ValueError('At least one parameter is required')

    #assing, and pass the last value as n    
    s = args.list
    n = s[len(s)-1]
    del s[-1]
    
    print sortedHasSum(s,n)
    
except ValueError:
    print 'Only numbers are accepted as parameters'
    



