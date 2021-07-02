a=[12, 34, 45, 9, 8, 90, 3]
eve= []
odd=[]
for i in range(0,len(a)):
    if(a[i]%2==0):
        eve.append(a[i])
    else:
        odd.append(a[i])
a.clear()
     
for i in range(len(eve)):
    a.append(eve[i])
for j in range(len(odd)):
    a.append(odd[j])
print(a)     
             