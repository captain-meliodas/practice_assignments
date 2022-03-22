def sortBinaryArray(A):
    zeroes = A.count(0)
    k = 0
    while zeroes:
        A[k] = 0
        k+=1
        zeroes-=1

    for i in range(k,len(A)):
        A[i] = 1
    

if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sortBinaryArray(A)
 
    # print the rearranged list
    print(A)