import random

#ar  = [6,11,7,12,18,3,15,2,9,14]
ar  = [10,11,7,12,18,3,15,2,9,14]
print(ar)

def change_position(A, i, j):
  if i != j:
    A[i] = A[i] ^ A[j]
    A[j] = A[j] ^ A[i]
    A[i] = A[i] ^ A[j]

def Partition(A,p,r):
  x = A[p-1]
  i = p-1
  j = r+1
  while True:
    while True:
      j -= 1
      if A[j-1] <= x:
        break
    while True:
      i += 1
      if A[i-1] >= x:
        break
    if i<j:
      change_position(A,i-1,j-1)
    else:
      return j

def Quicksort(A,p,r):
  if p < r:
    q = Partition(A,p,r)
    Quicksort(A,p,q)
    Quicksort(A,q+1,r)

def RandPartition(A,p,r):
  k = random.randint(p,r)
  change_position(A,p-1,k-1)
  return Partition(A,p,r)
  
def RandQuicksort(A,p,r):
  if p < r:
    q = RandPartition(A,p,r)
    RandQuicksort(A,p,q)
    RandQuicksort(A,q+1,r)

RandQuicksort(ar,1,len(ar))
print(ar) 
