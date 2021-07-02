def feb(n):
    first = 0
    second = 1
    
    n = int(input("n:-"))
    for i in range(n):
        print(first)
        temp = first
        first = second
        second = temp + first