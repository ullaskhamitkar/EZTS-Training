l=[2,4,3,4,6,7,1,2,5]
sum = max = 0
k=int(input('Enter the number: '))
for i in range(0,len(l)-k-1):
    sum =0
    for j in range(0,k):
        sum += l[i+j]
    # sum = l[i]+l[i+1]+l[i+2]
    if max<sum:
        max = sum
        pos = i
for j in range(0,k):
    print(l[pos+j])
print(max)