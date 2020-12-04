#storing values of whole numbers in list
listNumWhole = []

class DerivedList(list):
    def insertAtLastLocation(self,obj):
        self.__iadd__([obj])    
 
lstWhole=DerivedList(listNumWhole)

def DecToBin(num):
    if num > 1:
        DecToBin(num // 2)
        num = num % 2
    
    #adding values in list
    lstWhole.insertAtLastLocation(num)

# decimal number
number = int(input("Enter a decimal number: "))

DecToBin(number)

#printing of list without brackets and space
print ("Binary equivalent: ", *lstWhole, sep = "")
