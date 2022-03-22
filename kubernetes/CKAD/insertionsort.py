A = [1,34,21,3,5,1,2,11]

for i in range(1,len(A)):
    for j in range(i-1,0,-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
        else:
            break
print(A)

# python function to sort (sorting tuples list and sets)
# python function to reverse list, tuples and sets and sort the same
# python function to get permutations of strings (from collection import itertools)
# matrix multiplication in python