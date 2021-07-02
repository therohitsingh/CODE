n = [5,7,7,8,8,10]
x = int(input())
c = []
if x in n:
    for i in range(0,len(n)):
        if(x==n[i]):
            c.append(i)
else:
    c.append(-1)
    c.append(-1)    
print(c)    