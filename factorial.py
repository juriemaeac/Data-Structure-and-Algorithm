'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
num = input("Enter a number: ")

if num.isdigit():
    def recur_factorial(n):
        
            if n == 1:
                return n
            elif n < 1:
                return ("factorial does not exist for negative numbers")
            else:
                return n*recur_factorial(n-1)
        
    print ("The factorial of",num, "is",recur_factorial(int(num)))

else:
        print("Invalid Input. Integers only.")