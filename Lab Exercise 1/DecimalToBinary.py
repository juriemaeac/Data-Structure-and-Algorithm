num = int(input("Enter a decimal number: "))

#Empty string to hold the binary form of the number
b = ""

while num != 0:
    if (num % 2) == 1:
        b += "1"
    else:
        b += "0"

    #this is equivalent to num = num // 2 ----- num/=2 results to decimal
    #use double slash to result in integer
    num//=2

#b[::-1] is used to reverse all the elements
b = b[::-1]
print("Binary equivalent: "+str(b))

