
def maxSubarray(nums,length,target):
    res = []
    for i in range(length):
        result = []
        sum_ = nums[i]
        result.append(nums[i])
        if sum_ == target:
            return [result]
        for j in range(i+1,length):
            sum_ += nums[j]
            result.append(nums[j])
            if sum_ == target and result not in res:
                res.append(result) 
                break
    return res

# nums = [5, 6, -5, 5, 3, 5, 3, -2, 0 ]
nums = [8,-9, 10, -2, -10, 6, 18, 17 ]
target = 17
maxArray = []
temp = maxSubarray(nums,len(nums),target)
for i in temp:
    if len(maxArray) < len(i):
        maxArray = i
print(maxArray)