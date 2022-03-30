# oct = input()
# dec = int(oct,8)
# # print(int(binary,2)," ",hex(int(binary,2))[2:])
# print(" ",bin(dec))
from itertools import permutations
X = 'ABC'
Y = 'DABC'
temp = [''.join(i) for i in list(permutations(list(X)))]
if Y in temp:
    print(True)
else:
    print(False)