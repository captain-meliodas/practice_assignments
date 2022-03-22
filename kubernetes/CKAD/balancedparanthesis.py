inputData = input()
temp = ['']
paranthesis = {"{":"}","(":")","[":"]"}
for i in range(len(inputData)):
    if paranthesis.get(temp[-1],'y') == inputData[i]:
        temp.pop()
    else:
        temp.append(inputData[i])
print(temp)
if len(temp) == 1:
    print("Balanced")
else:
    print("Not Balanced")

# For each input string, print “MISSMATCH” if the nesting of brackets are not matching.  "TOO MANY OPENING"  if more opening brackets then the closing. "TOO MANY CLOSING" if more closing brackets than the opening brackets.  Else if everything is fine print "VALID". Finally terminated by newline charater. 