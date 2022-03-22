def get_pivot(A,first,last):
    mid = (first+last)//2
    pivot = last
    if A[first] < A[mid]:
        if A[mid] < A[last]:
            pivot = mid
        elif A[first] < A[last]:
            pivot = first
    return pivot


def partition(A,first,last):
    pivotIndex = get_pivot(A,first,last)
    pivotValue = A[pivotIndex]
    A[pivotIndex],A[first] = A[first],A[pivotIndex]
    border = first

    for i in range(first, last+1):
        if A[i] < pivotValue:
            border += 1
            A[i],A[border] = A[border],A[i]
    A[border],A[first] = A[first],A[border]

    return border

def quickSort(A,first,last):
    if first < last:
        p = partition(A,first,last)
        quickSort(A,first,p-1)
        quickSort(A,p+1,last)

A = [1,34,21,3,5,1,2,11]
quickSort(A, 0, len(A)-1)
print(A)