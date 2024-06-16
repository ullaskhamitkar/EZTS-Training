from stack import stack
e="[3+7{52/11(3+5)}]"
f = 0
S=stack()
ob='[{('
cb=')}]'
for i in e:
    if i in ob:
        S.push(i)
    if i in cb:
        x = S.pop()
        if x == '(' and i == ')':
            pass
        elif x == '{' and i == '}':
            pass
        elif x == '(' and i == ')':
            pass
        else:
            f = 1
            break      
if (f==0):
    print(True)
else:
    print(False)