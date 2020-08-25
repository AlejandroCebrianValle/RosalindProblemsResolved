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

### Auxiliar function
def readRosalindArchive(nameFile):
   lines = []
   with open(nameFile, "r") as fileContent:
      for line in fileContent:
         lines.append(line.replace("\n", "").split())
   lines[0] = int("".join(lines[0]))
   lines[1] = int("".join(lines[1]))
   lines[2] = [int(x) for x in lines[2]]
   lines[3] = [int(y) for y in lines[3]]
   return lines
### Binary search function
def binarySearch(array, item):
   init = 0
   end = len(array) - 1
   index = -1
   while init <= end:
      mid = (init + end) // 2
      if item == array[mid]:
         index = mid
         break
      else:
         if item < array[mid]:
            end = mid -1
         else:
            init = mid + 1
   return index

##############################################################################
## Probe section
if __name__ == "__main__":
   print("Recusive:\t", recursiveFibonacciSeq(9),
         recursiveFibonacciSeq(22))
   print("Dynamic programation:\t", dynamicPFibonacciSeq(9),
         dynamicPFibonacciSeq(22))
   print("Matrix:\t", matrixFibonacciSeq(9), matrixFibonacciSeq(22))
   dataset = readRosalindArchive("rosalind-BinarySearch.txt")
   results = []
   for elem in dataset[3]:
      index = binarySearch(dataset[2], elem)
      if index != -1:
         index += 1
      results += [index]
   print(" ".join([str(result) for result in results]))
