inp = input().split(" ")
k = int(input())
res = []
# for i in range(len(inp)-1):
#     if not (int(inp[i]) + k) == int(inp[i+1]):
#         res.append(int(inp[i]))
i = 0
start = len(inp)-1
end = 0
while i < len(inp)-1:
    curr = i
    if int(inp[i]) + k == int(inp[i+1]):
        # inp.pop(i)
        if start > i:
            start = i
        if end < i+1:
            end = i+1
        i = 0
    else:
        i += 1

print(inp,start,end)
