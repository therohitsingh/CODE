
#dynamic programming method 
def fib(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fib(9))        

#normal recursion method 
def fibn(n):
    if n<0:
        print("Incorrect Input")
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(9))        
        
#second method to do same thing 

def fiba(n):
    a = 0
    b = 1

    if n<0:
        print("Incorrect Input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2,n+1):
            c = a+b
            a,b = b,c
        return b 
print(fib(9))                   

#fourth 
def feb(n):
    first = 0
    second = 1
    
    n = int(input("n:-"))
    for i in range(n):
        print(first)
        temp = first
        first = second
        second = temp + first