A = [1,34,21,3,5,1,2,11]

for i in range(0,len(A)-1):
    minIndex = i
    for j in range(i+1, len(A)):
        if A[j] < A[minIndex]:
            minIndex = j
    if minIndex != i:
        A[i],A[minIndex] = A[minIndex],A[i]

print(A)
