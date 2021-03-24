'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 12, 2021]
'''
print("="*45)
print("\t\tSTRING COPY")
print("="*45)

str1 = input("Enter First Word (str1): ")
str2 = input("Enter Second Word (str2): ")
if str1.isdigit() or str2.isdigit():
        print ('Invalid input. String only.')
else:
    
    def strcpy (str1,str2):
        str1 = str2
        return str1
    print("-"*45)
        
    
    print ("The new string value for str1:",strcpy (str1,str2))
    print("-"*45)

    
