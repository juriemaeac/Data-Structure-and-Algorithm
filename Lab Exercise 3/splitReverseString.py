'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
import re
w = input("Enter a string: ")

if re.match(r"^[A-Za-z -.]+$", w):
    words = w.split(' ')
    arr = [(words) for words in words]

    for i in range(len(arr)-1, -1, -1):
        print (arr[i], sep = "\n")

else:
    print("Please input string only.")