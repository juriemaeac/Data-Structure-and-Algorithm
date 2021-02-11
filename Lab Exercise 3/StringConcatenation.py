'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
print("="*45)
print("\t  STRING CONCATENATION")
print("="*45)

str1 = input("Enter First Word: ")
str2 = input("Enter Second Word: ")
if str1.isdigit() or str2.isdigit():
        print ('Invalid input. String only.')
else:
    def strcat (str1, str2):
        print("-"*45)
        str3 = " "
        newVal = str1 + str3 + str2
        return newVal

    print ("The new string value is:", strcat (str1, str2))
    print("-"*45)
