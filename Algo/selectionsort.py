import sys
a = []
n = int(input("Enter the no. of elements in array:-"))

for i in range(0,n):
    m = int(input("Enter the Elements:-"))
    a.append(m)
    
for j in range(0,n):
    min = j
    for k in range(j+1,n):
        if a[min]>a[k]:
            min = k

    a[j],a[min]=a[min],a[j]


print("Selection Sort array is:-")
for i in range(0,n):
    print(a[i])            
                

