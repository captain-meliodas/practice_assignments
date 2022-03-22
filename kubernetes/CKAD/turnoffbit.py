# 2
# 15 4
# 15 1
def turnOffBit(num,k):
    if num < 0:
        #number should be greater than 0
        return n
    
    return num & ~(1 << (k-1))

testCases = int(input())
inputData = []
while(testCases):
    num,k = input().split(" ")
    inputData.append((int(num),int(k)))
    testCases-=1
    
i = 0
while(i < len(inputData)):
    num,k = inputData[i]
    result = turnOffBit(num,k)
    print(result)
    i += 1

