
class SieveOfEratosthenes:
    
    def __init__(self, sieveSize):
        self.sieveSize = sieveSize
        
    def initialiseSieve(self):
        self.couldBePrime = [True]*(self.sieveSize+1);
        self.couldBePrime[0] = False
        self.couldBePrime[1] = False
        self.nextNumberToCheck = 0
        
    def generatePrimes(self):
        self.initialiseSieve()
        pastTheSquareRootOfSize = False
        while self.nextNumberToCheck <= self.sieveSize:
            if self.couldBePrime[self.nextNumberToCheck]:
                prime = self.nextNumberToCheck
                if not pastTheSquareRootOfSize:
                    if prime*prime > self.sieveSize:
                        pastTheSquareRootOfSize = True
                    if not pastTheSquareRootOfSize:
                        self.markMultiplesNotPrime(prime)
                yield prime
            self.nextNumberToCheck += 1
            
    def markMultiplesNotPrime(self, prime):
        multipleOfPrime = prime*prime
        while (multipleOfPrime <= self.sieveSize):
            self.couldBePrime[multipleOfPrime] = False
            multipleOfPrime += prime
            
def main():
    SIZE = 3000000
    sieve = SieveOfEratosthenes(SIZE)
    print ("Prime numbers up to %s:" % SIZE)
    outfile = open ('p%s.txt' %SIZE, 'w')
    for prime in sieve.generatePrimes():
        outfile.write("%d\n" % prime)

if __name__ == "__main__":
    main()
