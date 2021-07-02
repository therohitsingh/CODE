def prime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                print("Not Prime")
                break
        else:
            print("Is Prime")

n = int(input("Enter the no:-"))
prime(n)