def manmohan(n):
    for i in range(0,n):
        if(i%2==1):
            for j in range(1,i):
                print("1")
        else:
            print("1")
            for j in range(0,i-2):
                print("0")
            print("1")
        print("\r")
n = 5
manmohan(n)                
