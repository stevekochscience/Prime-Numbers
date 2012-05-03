# Code is public domain--Steven J. Koch

# this R code requires a special csv file listing primes, loneliness, and swiss prime flag.
# I create this file with python code, "calclonelyfromprimes2.py"
# read in the prime numbers. first column is prime number, second column is loneliness, third column is a flag for whether it is a swiss
# prime. 1 = true, 0 = false, and -1 means there was only one neighbor.
lonely <- read.table("ls30000000.csv", sep=",", header=FALSE)  
names(lonely) <- c("prime", "lness", "swiss")

# find subset of "Swiss primes."  I.e. those primes that are equidistant between the two neighboring prime numbers
swiss <- subset(lonely, swiss == 1)


#save the graph to a PNG file
#png("30M swiss prime loneliness.png")

# create the plot
plot(lonely$prime, lonely$lness, log="x", pch=1, cex=0.5, main="Prime loneliness", xlab="number", ylab="loneliness",
      ylim = c(0, max(lonely$fit, lonely$lness)))
points(swiss$prime, swiss$lness, pch=21, cex=1.1, col="magenta")

legend("topleft", c("Loneliness, all primes", "Loneliness, Swiss primes"), pch = c(1, 21),
       col = c("black", "magenta"), inset = 0.1)
                                                              
# this next command is necessary to make the graph save, I don't know why.  It makes the graph disappear from the screen though
# I also have trouble viewing the file with external editor unless I close out of R.  Obviously doing something wrong.
#dev.off()

