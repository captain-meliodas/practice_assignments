a = input()
b = input()
CHARS = 26
def makeAnagram(a,b):
    str_1 = [0] * CHARS
    str_2 = [0] * CHARS

    i = 0
    while (i < len(a)):
        str_1[ord(a[i]) - ord('a')] += 1
        i+=1
    
    i = 0
    while (i < len(b)):
        str_2[ord(a[i]) - ord('a')] += 1
        i+=1
    
    result = 0
    for i in range(CHARS):
        result += abs(str_1[i] - str_2[i])
    return result

print(makeAnagram(a,b))