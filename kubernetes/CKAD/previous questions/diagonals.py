row,col = map(int,input().split(" "))
suma = 0
sumb = 0
# matrix = 0
for r in range(row):
    cols = list(map(int,input().split(" ")))
    # suma += cols[r]
    for c in range(col):
        if r == c:
            suma += cols[r]
            sumb += cols[((len(cols)-1) - c)]

print(abs(suma-sumb))

# Input
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9