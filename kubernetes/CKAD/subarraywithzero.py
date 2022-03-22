def subArrayExistsHash(arr,n):
    hash_ = set()
    total = 0
    for i in arr:
        total += i

        if total == 0 or total in hash_:
            return True
        hash_.add(total)
    return False

def subArrayExistsBruteForce(arr,n):
    total = 0
    for i in range(n-1):
        total = arr[i]
        for j in range(i+1,n):
            total += arr[j]
            if total == 0:
                print(i,j)
                # return True
    return False


arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
n = len(arr)
if subArrayExistsBruteForce(arr, n) == True:
    print("Found a sunbarray with 0 sum")
else:
    print("No Such sub array exits!")

if subArrayExistsHash(arr, n) == True:
    print("Found a sunbarray with 0 sum")
else:
    print("No Such sub array exits!")