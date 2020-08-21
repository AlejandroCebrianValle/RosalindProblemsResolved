## Recursive Function to Fibonacci sequence
def recursiveFibonacciSeq(n):
   if n == 0:
     return 0
   elif n == 1:
     return 1
   else:
     return recursiveFibonacciSeq(n - 1) + recursiveFibonacciSeq(n - 2)
## Binary Search in file
### Auxiliar Functions
def readDocuments(nameFile):
   with open(nameFile, 'r') as file:
      lines = file.readlines()
   data = list()
   for line in lines:
      data.append(line.replace("\n", ""))
   return data

## Degree Array
import networkx as nx
import matplotlib.pyplot as plt

def DegreeEdgesInText(nameFile):
   G = nx.read_edgelist(nameFile, nodetype = int)
   degreeList = list()
   for node in list(G.nodes):
      degreeList.append(len(list(G.neighbors(node))))
   return degreeList

## Probe section
if __name__ == "__main__":
   print(recursiveFibonacciSeq(6)) # 8
   print(recursiveFibonacciSeq(9)) # 34
   print(recursiveFibonacciSeq(22)) # 17711
   print(*DegreeEdgesInText("Rosalind-DegreeArray.txt"), sep=" ")
