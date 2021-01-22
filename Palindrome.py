'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
import re
x = input("Enter a word: ")

#x[::-1] is used to reverse all the elements
#source lesson: https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html

#library that accepts word with some symbols and spaces only 
# since some of names/ words are with symbols
if re.match(r"^[A-Za-z -.]+$", x):
    y = x[::-1]
    if x == y:
        print(x, "is a palindrome")
    else:
        print(x, "is not a palindrome")
else:
    print ("This is not a word")
