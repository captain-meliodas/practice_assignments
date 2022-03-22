def balance_sorted_lists(a, b):                          # <---  Function header
    '''
    Returns the balanced list after swapping two values  # <--- Purpose
    
    balance_sorted_lists: List List -> List              # <--- Contract

    Eamples:
        balance_sorted_lists([153284], [153285]) => None
        balance_sorted_lists([-3, 1, 2, 3], [6, 7, 8, 12]) => [0, 3]
        balance_sorted_lists([1, 3, 3, 4, 6, 8, 8, 8, 10], [1, 1, 2, 2, 7, 7, 7, 7, 15]) => [1, 2]
    
    '''
    
    
    flag=0                                              # <--- Function body
    for i in a:
        if i<0:
            flag=1
    for i in b:
        if i < 0:
            flag = 1
    sum1 = sum(a)
    sum2 = sum(b)
    diff = abs(sum1-sum2)
    dif = []
    ind=[]
    # print(diff)
    for i in range(len(a)):
        if diff - abs(a[i]) not in dif:
            dif.append(diff - abs(a[i]))
            ind.append(i)
    # print(dif)
    # print(ind)
    for i in range(len(b)):
        if(flag==1):
            if diff//2 + b[i] in dif:
                return [ind[dif.index(diff//2 + b[i])], i]
        elif(flag==0):
            if diff//2 - b[i] in dif:
                return [ind[dif.index(diff//2 - b[i])], i]
        else:
            None
    else:
        return None

def sort_list(a,b):
    suma=sum(a)
    sumb=sum(b)
    print(suma,sumb)
    temp = []
    for i in range(len(a)):
        for j in range(len(b)):
            print((suma,a[i],b[j],suma-a[i]+b[j]),(sumb,b[j],a[i],sumb-b[j]+a[i]))
            if((suma-a[i]+b[j])==(sumb-b[j]+a[i])):
                # print((suma,a[i],b[j]), (sumb,b[j],a[i]))
                return [i,j]
            temp.append(a[i]+b[j])
            temp.append(b[j]+a[i])
    return None

# print(sort_list([1,3,4,17],[2,4,5,6]))
#  -1 -1 -1 11
# 25 17
# print(sort_list([153284], [153285]))
print(sort_list([-3, 1, 2, 3], [6, 7, 8, 12])) 
                 0   1  2  3    0  1  2   3
# -9 -6 -6 -9
# 3 33
# print(sort_list([1, 3, 3, 4, 6, 8, 8, 8, 10], [1, 1, 2, 2, 7, 7, 7, 7, 15]))
# 0 2 1 2 1 1 1 1 5


## Other tests:
# print(balance_sorted_lists([3,7,7], [2,3,5])) # iska answer [0,0
# ## Example as tests:
# print(balance_sorted_lists([153284], [153285]))
# print(balance_sorted_lists([-3, 1, 2, 3], [6, 7, 8, 12]))
# print(balance_sorted_lists([1, 3, 3, 4, 6, 8, 8, 8, 10], [1, 1, 2, 2, 7, 7, 7, 7, 15]))

# ## Other tests:
# print(balance_sorted_lists([3,7,7], [2,3,5])) # iska answer [0,0