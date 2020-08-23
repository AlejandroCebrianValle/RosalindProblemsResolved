##############################################################################
##
##             Fibonacci Sequence
##
##############################################################################

## Recursive Function to Fibonacci sequence
def recursiveFibonacciSeq(n):
   if n == 0:
     return 0
   elif n == 1:
     return 1
   else:
     return recursiveFibonacciSeq(n - 1) + recursiveFibonacciSeq(n - 2)
     
## Dynamic Programation
def dynamicPFibonacciSeq(n):
   fArray = [0,1]
   for i in range(2, n + 1, 1):
      fArray += [fArray[i - 1] + fArray[i - 2]]
   return fArray[n]

## Matrix calculus
def matrixFibonacciSeq(n):
   F = [[1, 1],
        [1,0]]
   if n == 0:
      return 0
   else:
      M = [[1, 1],
           [1,0]]
      for i in range(2, n):
         x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
         y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
         z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
         w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
         ## 
         F[0][0] = x 
         F[0][1] = y 
         F[1][0] = z 
         F[1][1] = w
   return F[0][0]

##############################################################################
##
##             Binary Search in file
##
##############################################################################



## Probe section
if __name__ == "__main__":
   print(recursiveFibonacciSeq(9), recursiveFibonacciSeq(22))
   print(dynamicPFibonacciSeq(9), dynamicPFibonacciSeq(22)) 
   print(matrixFibonacciSeq(9), matrixFibonacciSeq(22)) 
