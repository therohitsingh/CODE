def bubblesort(a):
    n = len(a)
    for i in range(n):

        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

if __name__ == "__main__":
    a = []
    n = int(input("Enter the number of elements in array:-"))
    for i in range(0,n):
        m = int(input("Enter the elements:-"))
        a.append(m)
    bubblesort(a)    
    print("Sorted array is :-")
    for i in range(len(a)):
        print(a[i])    


