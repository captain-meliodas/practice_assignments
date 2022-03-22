import sys
def minCoins(coins,m,v):
    table = [0 for i in range(v+1)]
    table[0] = 0
    for i in range(1,v+1):
        table[i] = sys.maxsize

    for i in range(1,v+1):
        for j in range(m):
            if(coins[j] <= i):
                sub_res = table[i - coins[j]]
                if(sub_res != sys.maxsize and sub_res+1 < table[i]):
                    table[i] = sub_res + 1
    print(table)
    if table[v] == sys.maxsize:
        return -1
    return table[v]

coins = [9,6,5,1]
m = len(coins)
sum_ = 12

print(minCoins(coins,m,sum_))