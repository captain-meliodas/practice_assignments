import sys
MAX_INT = sys.maxsize

def merge(A,first,mid,last):
    L = A[first:mid+1]
    R = A[mid+1:last+1]
    L.append(MAX_INT)
    R.append(MAX_INT)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

def mergeSort(A,first,last):
    if first < last:
        mid = (first+ last) // 2
        mergeSort(A,first,mid)
        mergeSort(A,mid+1,last)
        merge(A,first,mid,last) 

A = [1,34,21,3,5,1,2,11]
mergeSort(A, 0, len(A)-1)
print(A)