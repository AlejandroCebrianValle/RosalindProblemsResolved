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

## Binary search
