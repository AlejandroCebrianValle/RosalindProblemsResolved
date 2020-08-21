## Recursive Function to Fibonacci sequence
def recursiveFibonacciSeq(n):
   if n == 0:
     return 0
   elif n == 1:
     return 1
   else:
     return recursiveFibonacciSeq(n - 1) + recursiveFibonacciSeq(n - 2)
 

## Probe section
if __name__ == "__main__":
   print(recursiveFibonacciSeq(0)) # 0
   print(recursiveFibonacciSeq(1)) # 1
   print(recursiveFibonacciSeq(6)) # 8
   print(recursiveFibonacciSeq(9)) # 34
   print(recursiveFibonacciSeq(22)) # 17711
