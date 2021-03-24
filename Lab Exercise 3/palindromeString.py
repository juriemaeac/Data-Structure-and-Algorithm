'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 12, 2021]
'''
import re
z = input("Enter a word: ")
x = z.lower()

if re.match(r"^[A-Za-z -.]+$", x):
    y = x[::-1]
    if x == y:
        print(z, "is a palindrome")
    else:
        print(z, "is not a palindrome")
else:
    print ("This is not a word")