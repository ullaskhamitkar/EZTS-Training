def fib_num(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    fib_sequence=[0,1]
    for i in range(2,n):
        next_value=fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence
    
print(fib_num(10))