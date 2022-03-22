
def findPair(arr,n,sum_):
    if sum_ == 0:
        return 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i]+arr[j] == sum_:
                print(arr[i],arr[j])
                return
    print("Not Found")

nums = [335,501,170,725,479,359,963,465,706,146,282,828,962,492,996,943,828,437,392,605,903,154,293,383,422,717,719,896,448,727,772,539,870,913,668,300,36,895,704,812,323,334]
target= 468
findPair(nums,len(nums),target)