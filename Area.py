'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
print("="*45)
print("\t\t\t\t\tMENU")
print("="*45)
print("[1] Area of Square")
print("[2] Area of Rectangle")
print("[3] Area of Triangle")
print("[4] Area of Circle")
print("[5] Exit")
print("-"*45)

num = (input("Enter your choice: "))
if num.isdigit():
  if num == 1:
    print("COMPUTING FOR AREA OF SQUARE...")
    side = int(input("\nEnter the side of square: "))
    areaS = side*side
    print("-"*45)
    print("The area of square is ", areaS, " sq. units.")
    print("_"*45)
  elif num == 2:
    print("COMPUTING FOR AREA OF RECTANGLE...")
    w, l = map(int, input("\nEnter width and length of rectangle: ").split())
    areaR = w*l
    print("-"*45)
    print("The area of rectangle is", areaR, "sq. units.")
    print("_"*45)
  elif num == 3:
    print("COMPUTING FOR AREA OF TRIANGLE...")
    b, h = map(int, input("\nEnter base and height of triangle: ").split())
    areaT = (1/2)*b*h
    print("-"*45)
    print("The area of triangle is", areaT, "sq. units.")
    print("_"*45)
  elif num == 4:
    print("COMPUTING FOR AREA OF CIRCLE...")
    r = int(input("\nEnter the radius of circle: "))
    areaC = 3.14*(r*r)
    print("-"*45)
    print("The area of circle is", areaC, "sq. units.")
    print("_"*45)
  elif num == 5:
    exit()
  else:
    print("\nInvalid input please choose above.")
    print("_"*45)
else:
  print("\nInvalid input please choose above.")
  print("_"*45)