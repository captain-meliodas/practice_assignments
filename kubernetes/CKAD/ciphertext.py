value = input()
cipherValue = 1
encodedStrng = ''
small_a = 'abcdefghijklmnopqrstuvwxyz'
cpital_a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in value:
    if cipherValue % 2 == 0:
        if i in small_a:
            encodedStrng += small_a[((small_a.index(i) - (cipherValue%26)))%26]
        
        if i in cpital_a:
            encodedStrng += cpital_a[((cpital_a.index(i) - (cipherValue%26))%26)]
    else:
        if i in small_a:
            encodedStrng += small_a[((small_a.index(i) + (cipherValue%26)))%26]
        
        if i in cpital_a:
            encodedStrng += cpital_a[((cpital_a.index(i) + (cipherValue%26)))%26]
    
    cipherValue += 1
print(encodedStrng)


