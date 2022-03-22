mystring = input()
pattern = input()

i = j = k = 0
flag = 0
if pattern == '*':
    flag = 0
elif pattern == '?' and len(mystring) == 1:
    flag = 0
elif pattern == '?' and len(mystring) > 1:
    flag = 1
else:
    while i < len(mystring):
        print(i,j, k)
        if mystring[i] == pattern[j]:
            i+=1
            j+=1
        
        elif pattern[j] == '*':
            k = j
            while pattern[k] == '*':
                k+=1
            if pattern[k] != mystring[i]:
                i+=1
            else:
                j+=1

        elif pattern[j] == '?':
            i+=1
            j+=1
        else:
            flag = 1
            break

if flag:
    print(False)
else:
    print(True)
