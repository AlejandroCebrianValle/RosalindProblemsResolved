rm = list(ls())

##############################################################################
##
##             Fibonacci Sequence
##
##############################################################################

## Recursive Function to Fibonacci sequence
recursiveFibonacciSequence <- function(n){
  if(n == 0) {
    return(0)
  }
  if(n == 1) {
    return(1)
  }
  else {
    return(recursiveFibonacciSequence(n-1) + recursiveFibonacciSequence(n-2))
  }
}
## Dynamic Programation
dynamicPFibonacciSequence <- function(n){
  fArray <- c(0, 1)
  for (i in 2:(n + 1)){
    fArray <- append(fArray, (fArray[i - 2] + fArray[i - 1]));
  }
  return(fArray[n + 1])
}
## Matrix calculus
matrixFibonacciSeq <- function(n){
  fMatrix <- matrix(c(1,1,1,0), nrow = 2, ncol = 2);
  if (n == 0){
    return(0)
  } else {
    mMatrix <- matrix(c(1,1,1,0), nrow = 2, ncol = 2);
    for (i in 2:(n - 1)){
      fMatrix <- fMatrix %*% mMatrix;
    }
    return(fMatrix[1][1])
  }
}

## Probe Section
cat(sprintf("Recusive:\t%d\t%d\n", recursiveFibonacciSequence(9),
            recursiveFibonacciSequence(22)))
cat(sprintf("Dynamic Programation:\t%d\t%d\n", dynamicPFibonacciSequence(9),
            dynamicPFibonacciSequence(22)))
cat(sprintf("Matrix:\t%d\t%d\n", matrixFibonacciSeq(9),
            matrixFibonacciSeq(22)))

##############################################################################
##
##             Binary Search in file
##
##############################################################################

### Binary search function
binarySearch <- function(arraySearch, item){
  lowValue <- 0;
  maxValue <- length(arraySearch) - 1;
  index <- -1;
  while (lowValue <= maxValue){
    mid = (lowValue + maxValue) %/% 2;
    if (item == arraySearch[mid]){
      index = mid;
      break;
    } else {
      if (item < arraySearch[mid]){
        maxValue <- mid - 1;
      } else {
        lowValue <- mid + 1;
      }
    }
  }
  return(index);
}
### Probe Section
##### First, we read the archive. The Unique important section is the 3rd and 
##### 4th line.
fileLines <- readLines("rosalind-BinarySearch.txt");
arrayOrdered <- as.numeric(unlist(strsplit(fileLines[3]," ")));
arrayUnordered <- as.numeric(unlist(strsplit(fileLines[4]," ")));
##### Second, lets search...
results <- c();
for (element in arrayUnordered) {
  results <- append(results, binarySearch(arrayOrdered, element));
}
cat(results)
