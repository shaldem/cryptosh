#сортировка подсчетом
# применим для сортировки массива целых чисел,
# о которых известно, что они меньше k

def counting_sort(A,B,k):
  C = []
  i,j = 0,0

  while i < k:
    C.append(0)
    i+=1
  
  while j < len(A):
    C[A[j]] += 1
    j+=1
  
  i=1
  while i < k:
    C[i] += C[i-1]
    i+=1

  while j > 0:
    j-=1
    B[C[A[j]]-1] = A[j]
    C[A[j]]=C[A[j]]-1
    


A = [26,60,7,31,42,74,93,0,44,42,11]
B = A.copy()
k = 100
print(A)
counting_sort(A,B,k)
print(B)