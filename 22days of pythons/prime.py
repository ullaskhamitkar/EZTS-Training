def primeNum(num):
    if num<0:
        return False
    elif num==0 and num ==1:
        return True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

print(primeNum(12))
