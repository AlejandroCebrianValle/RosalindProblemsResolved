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

## Probe section
recursiveFibonacciSequence(0) # 0
recursiveFibonacciSequence(1) # 1
recursiveFibonacciSequence(6) # 8
recursiveFibonacciSequence(9) # 34
recursiveFibonacciSequence(22) # 17711

## Binary search
