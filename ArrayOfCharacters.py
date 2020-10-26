x = input("Enter a word: ")

#x[::-1] is used to reverse all the elements
#source lesson: https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html

y = x[::-1]

if x == y:
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")