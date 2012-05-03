# this file reads a prime number file (each number in own row) and calculates loneliness

import math

SIZE = 30000000

def loneliness(mylist, i):
    """If the number is at the edge of the list, swiss flag is set to -1.  Otherwise, 1 means true and 0 means false.
       The lness is the loneliness which is geometric mean of distance between neighboring primes.  If these distances
       are equal it will be "1" for true as swiss.  If lness is an integer, it means that the two distances combined have an
       an even number of each divisor.  For example, distances = 2 and 50."""
    # print i, mylist[i]
    if i == 0:
        lness = mylist[i+1]-mylist[i]
        swiss = -1
    elif i == (len(mylist) - 1):
        lness = mylist[i] - mylist[i-1]
        swiss = -1
    else:
        assert i>0 and i < len(mylist) - 1
        lness = math.sqrt( (mylist[i+1] - mylist[i]) * (mylist[i] - mylist[i-1]) )
        if mylist[i+1] - mylist[i] == mylist[i] - mylist[i-1]:
            swiss = 1
        else:
            swiss = 0
    return [lness, swiss]

primes=[]

fh = open("p%s.txt" %SIZE)

for line in fh:
    primes.append(int(line))

fh.close()

lonely = []
swiss = []
    
for j in range(0,len(primes)):
    result = loneliness(primes, j)
    lonely.append(result[0])
    swiss.append(result[1])
 
outfile = open ('ls%s.csv' %SIZE, 'w')

for j in range(0,len(primes)):
    outfile.write("%d,%f,%d\n" % (primes[j], lonely[j], swiss[j]))

outfile.close()

