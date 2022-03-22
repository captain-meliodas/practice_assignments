# Input
# 1 2 3
# 0 0 0
# 4 5 6
# 0 0 8
# Output
# 1 2 3
# 4 5 6
# 0 0 8

# [[],[],[],[]]

m = int(input())
n = int(input())
a = []
# flag = 0
for i in range(m):
    value = input().split(" ")
    b = []
    for j in value:
        temp = int(j)
        if temp != 0:
            b.append(temp)
    if len(b) != 0:
        a.append(value)
for i in a:
    for j in i:
        print(j, end=" ")
    print()