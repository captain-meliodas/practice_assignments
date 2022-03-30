#selection sort
print("----------selection sort-----------------------")
a = [4,3,2,1,4,5,1]
for i in range(len(a)):
    min_index = i #select the min index
    for j in range(i+1,len(a)):
        if a[min_index] > a[j]: #if value at min index is greater than next
            min_index = j #change the min index to min value index
    a[i],a[min_index] = a[min_index],a[i]
    print(a)

print("---------Insertion Sort---------")
a = [4,3,2,1,4,5,1]
for i in range(len(a)):
    key = a[i]
    j = i-1
    while j>=0 and key < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
    print(a)

print("---------Bubble Sort---------")
a = [7,6,5,4,3,2,1]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print(a)

print("---------Merge Sort---------")
a = [7,6,5,4,3,2,1]
import sys
MAX_INT = sys.maxsize
def merge(a,l,mid,r):
    L = a[l:mid+1]
    R = a[mid+1:r+1]

    L.append(MAX_INT)
    R.append(MAX_INT)
    i = 0
    j = 0
    for k in range(l,r+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            j+=1
        

def mergeSort(a,l,r):
    if l < r:
        mid = (l+r)//2
        mergeSort(a,l,mid)
        mergeSort(a,mid+1,r)
        merge(a,l,mid,r)
        res.append(a)
res = []
mergeSort(a,0,len(a)-1)
print(res)
print(a)

print("---------Quick Sort---------")
def partition(a,l,r):
    pivot = l
    pivotValue = a[pivot]
    border = l
    #put all values smaller than border index to left
    #put all values greater than border index to left
    for i in range(l,r+1):
        if a[i] < pivotValue:
            border+=1
            a[i],a[border] = a[border],a[i]
    a[border],a[l] = a[l],a[border]
    return border

def quickSort(a,l,r):
    if l < r:
        p = partition(a,l,r)
        quickSort(a,l,p-1)
        quickSort(a,p+1,r)

a = [7,6,5,4,3,2,1]
quickSort(a,0,len(a)-1)
print(a)

