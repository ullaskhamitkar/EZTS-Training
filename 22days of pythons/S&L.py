def primeNum(num):
    if num<0:
        return False
    elif num==0 and num ==1:
        return True
    for i in range(2,int(num//2)):
        if num%i==0:
            return False
    return True

def greaterNum(num):
    temp=num+1
    while True:
        if primeNum(temp):
            return temp
        temp+=1
def sumNum(num):
    next_prime=greaterNum(num)
    sum =0
    for i in range(num+1,next_prime):
        sum+=i
    return sum
def answer(num):
    nextNum1 = greaterNum(num)
    nextNum2 = sumNum(nextNum1)
    return primeNum(nextNum1*nextNum2)
def primeKey(num):
    return(greaterNum(num),sumNum(num),answer(num))
print(primeKey(int(input())))