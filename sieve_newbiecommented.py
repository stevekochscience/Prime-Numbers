
# SJK: This is my first time trying to understand a class
# (This class was written by someone else on github)
# I found the following tutorial useful: 
# mail.python.org/pipermail/tutor/2002-August/016388.html
class SieveOfEratosthenes:
    
    def __init__(self, sieveSize):
        self.sieveSize = sieveSize
        
    def initialiseSieve(self):
        self.couldBePrime = [True]*(self.sieveSize+1); # this initializes self.coudBePrime to be an array of True values, length = self.sieveSize + 1
        self.couldBePrime[0] = False
        self.couldBePrime[1] = False
        self.nextNumberToCheck = 0

# because this next function has a "yield," it is a generating function        
    def generatePrimes(self):
        self.initialiseSieve() #this calls the initialize function above, I guess since it's a generating function, this will only get called once.  But I find it confusing that the generating function intitializes, I'd rather it were initialized outside the method, but being a newbie, I don't know what is better or whether both would work.
        pastTheSquareRootOfSize = False
        while self.nextNumberToCheck <= self.sieveSize: # .nextNumberToCheck starts at 0, ends at .sieveSize
            if self.couldBePrime[self.nextNumberToCheck]: #check whether this number has already been marked as not prime by prior iteration.  There is no else for this if statement.  So, if it's already not prime, nothing happens and the nextNumberToCheck is incremented.
                prime = self.nextNumberToCheck
                if not pastTheSquareRootOfSize:
                    if prime*prime > self.sieveSize:
                        pastTheSquareRootOfSize = True
                    if not pastTheSquareRootOfSize:
                        self.markMultiplesNotPrime(prime)
                yield prime #the generator exits at this point, returning variable prime.  When it resumes, it resumes at the next line, with all local vaiables intact.  See python.org/dev/peps/pep-0255/
            self.nextNumberToCheck += 1 #increment .nextNumberToCheck
            
    def markMultiplesNotPrime(self, prime):
        multipleOfPrime = prime*prime # it is sufficient to start at prime * prime, since prior multiples will have already been marked
        while (multipleOfPrime <= self.sieveSize):
            self.couldBePrime[multipleOfPrime] = False
            multipleOfPrime += prime #after starting at prime * prime, mark each number that is an increment of prime higher, up until sieve size
            
def main():
    SIZE = 100
    sieve = SieveOfEratosthenes(SIZE)
    print ("Prime numbers up to %s:" % SIZE)
    outfile = open ('p%s.txt' %SIZE, 'w')
    for prime in sieve.generatePrimes(): # generatePrimes() is an iterable generating function in class SieveOfEratosthenes
        outfile.write("%d\n" % prime)

if __name__ == "__main__":
    main()
