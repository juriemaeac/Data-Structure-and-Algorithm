'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 7, 2021]
'''
import re

word = input("Enter some string: ")
if re.match(r"^[A-Za-z -.]+$", word):
    result = word.title()
    print(result)
else:
    print ("Error, String only.")