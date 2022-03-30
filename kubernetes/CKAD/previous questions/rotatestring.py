inpstring = input()
anticlockwise = list(inpstring)
clockwise = list(inpstring)
d = int(input())
#anticlockwise or right
for i in range(d%len(inpstring)):
    ele = anticlockwise.pop()
    anticlockwise.insert(0,ele)
#clockwise or left
for i in range(d%len(inpstring)):
    ele = clockwise.pop(0)
    clockwise.append(ele)
print(''.join(anticlockwise))
print(''.join(clockwise))