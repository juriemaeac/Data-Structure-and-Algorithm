'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
#storing values of whole numbers in list
listNumWhole = []

class DerivedList(list):
    def insertAtLastLocation(self,obj):
        self.__iadd__([obj])    
 
lstWhole=DerivedList(listNumWhole)

while True:
    Inputnumber = input("Enter a decimal number: ")
    try:
        num = int(Inputnumber)
        def DecToBin(num):
            val = int(num)

            #convertion
            if val > 1:
                DecToBin(val // 2)
                val = val % 2

            #adding values in list
            lstWhole.insertAtLastLocation(val)
        
        DecToBin(Inputnumber)

        #printing of list without brackets and space
        print ("Binary equivalent: ", *lstWhole, sep = "")
        break;

    except ValueError:
        try:
            float(Inputnumber)
            def FloatToBin(number, places = 3): 
  
                # split() seperates whole number and decimal
                whole, dec = str(number).split(".") 
  
                #converting whole and dec from str to int
                whole = int(whole) 
                dec = int (dec) 
  
                # Convert the whole number to binary form and remove the "0b" from it. 
                res = bin(whole).lstrip("0b") + "."
                if whole == 0:
                    res = bin(whole).lstrip("0b") + "0."

                # Iterating up to the desired number of decimal places to be 
                for x in range(places): 
  
                    #seperating the whole number and decimal part 
                    whole, dec = str((decimal_converter(dec)) * 2).split(".") 
  
                    # Convert from str to int
                    dec = int(dec) 
  
                    # Keep adding the integer parts  
                    # receive to the result variable 
                    res += whole 
  
                return res 

            #convertion
            def decimal_converter(num):  
                while num > 1: 
                    num /= 10
                return num 
            print("Binary equivalent: " + FloatToBin(Inputnumber, places = 10)) 
            break;

        except ValueError:
             print("This is not a number. Please enter a valid number")
