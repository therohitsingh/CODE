n = int(input("Enter the no:-"))
for i in range(n+1,0,-1):
    # inner loop to handle no. of columns
    # values is changing according to outerloop
    for j in range(0,i-1):
        print("* ",end="")


    print()    