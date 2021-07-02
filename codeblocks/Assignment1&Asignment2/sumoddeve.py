def getSum(n):
 
    # If n is odd then the last digit
    # will be odd positioned
    if (n % 2 == 1) :
        isOdd = True
    else:
        isOdd = False
 
    # To store the respective sums
    sumOdd = 0
    sumEven = 0
 
    # While there are digits left process
    while (n != 0) :
 
        # If current digit is odd positioned
        if (isOdd):
            sumOdd += n % 10
 
        # Even positioned digit
        else:
            sumEven += n % 10
 
        # Invert state
        isOdd = not isOdd
 
        # Remove last digit
        n //= 10
	 print(sumEven) 
     print(sumOdd)
   
 
# Driver code
if __name__ =="__main__":
    n = input()
    getSum(n)



if __name__=="__main__":
    n = int(input())
    getsum(n)