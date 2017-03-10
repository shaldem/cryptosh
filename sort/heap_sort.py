ar  = [6,11,7,12,18,3,15,2,9,14]
print(ar)

left = lambda i: (i<<1)|1
right = lambda i: (i+1)<<1
parent = lambda i: (i-1)>>1

max_heap = lambda a, b: a > b
min_heap = lambda a, b: a < b
heap_size = lambda A: len(A)

def change_position(A, i, j):
  if i != j:
    A[i] = A[i] ^ A[j]
    A[j] = A[j] ^ A[i]
    A[i] = A[i] ^ A[j]

def Heapify(A, heap_size, i, cmp):
  l = left(i)
  r = right(i)
  cur = i
  if l < heap_size and cmp(A[l],A[cur]):
    cur = l
  if r < heap_size and cmp(A[r], A[cur]):
    cur = r
  if cur != i:
    change_position(A,i,cur)
    Heapify(A, heap_size, cur, cmp)
	
def BuildHeap(A, cmp):
  i = int(len(A)/2 - 1)
  while i >= 0:
    Heapify(A, len(A), i, cmp)
    i-=1

BuildHeap(ar, max_heap)
print(ar)

def SortHeap(A, cmp):
  i = len(A)-1
  while i>0:
    change_position(A,0,i)
    Heapify(A,i,0,cmp)
    i-=1

SortHeap(ar, max_heap)
print(ar)