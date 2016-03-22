import sys,argparse
#Test
# 11 32 20 21 3 19 10 39 41 39

#quicksort with tail recursion
def quick_sort(a, s, e):
    while s < e:
        p=partition(a,s,e)
        quick_sort(a,s,p-1)
        s = s+1
        
#1st partition algorithm
def partition(array, s, e):
    pivot = s
    for i in xrange(s+1, e+1):
        if array[i] <= array[s]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[s] = array[s], array[pivot]
    return pivot
    

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
    
    quick_sort(s,0,len(s)-1)
    print s
    
except ValueError:
    print 'Only numbers are accepted as parameters'