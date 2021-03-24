'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 13, 2021]
'''
n1 = input("Enter number1: ")
if n1.isdigit():
    n2 = input("Enter number2: ")
    if n2.isdigit():
        x = max(n1, n2)

        def main():
            print("The greatest out of two numbers is",x)
            
        if __name__=="__main__":
            main()
    else:
        print("Invalid Input. Integers only.")
else:
    print("Invalid Input. Integers only.")

