'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
print("="*45)
print("\t  STRING COMPARISON")
print("="*45)

str1 = input("Enter First Word: ")
str2 = input("Enter Second Word: ")
if str1.isdigit() or str2.isdigit():
        print ('Invalid input. String only.')
else:
    def strcmp (str1,str2):
        print("-"*45)
        if str1 == str2:
            return "equal"
        elif str1 > str2:
            return "positive"
        elif str1 < str2:
            return  "negative"
        else:
            return

    print (strcmp (str1,str2))
    print("-"*45)
