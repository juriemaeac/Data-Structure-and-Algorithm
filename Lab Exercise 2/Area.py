'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 13, 2021]
'''
print("="*45)
print("\t\t     MENU")
print("="*45)
print("   [1]   Area of Square")
print("   [2]   Area of Rectangle")
print("   [3]   Area of Triangle")
print("   [4]   Area of Circle")
print("   [5]   Exit")
print("-"*45)

num = (input("Enter your choice: "))
if num.isdigit():
  opt = int(num)
  if opt == 1:
    print("COMPUTING FOR AREA OF SQUARE...")
    side = (input("\nEnter the side of square: "))
    if side.isdigit():
      areaS = side*side
      print("-"*45)
      print("The area of square is ", areaS, " sq. units.")
      print("_"*45)
    else:
      print("\nInvalid input.")
      print("_"*45)
  elif opt == 2:
    print("COMPUTING FOR AREA OF RECTANGLE...")
    w, l = map(input("\nEnter width and length of rectangle: ").split())
    if w.isdigit() and l.isdigit():
      areaR = w*l
      print("-"*45)
      print("The area of rectangle is", areaR, "sq. units.")
      print("_"*45)
    else:
      print("\nInvalid input.")
      print("_"*45)
  elif opt == 3:
    print("COMPUTING FOR AREA OF TRIANGLE...")
    b, h = map(input("\nEnter base and height of triangle: ").split())
    if b.isdigit() and h.isdigit(): 
      areaT = (1/2)*b*h
      print("-"*45)
      print("The area of triangle is", areaT, "sq. units.")
      print("_"*45)
    else:
      print("\nInvalid input.")
      print("_"*45)
  elif opt == 4:
    print("COMPUTING FOR AREA OF CIRCLE...")
    r = (input("\nEnter the radius of circle: "))
    if r.isdigit():  
      areaC = 3.14*(r*r)
      print("-"*45)
      print("The area of circle is", areaC, "sq. units.")
      print("_"*45)
    else:
      print("\nInvalid input.")
      print("_"*45)  
  elif opt == 5:
    print("Thank you!")
    input("\nPress any key to exit...")
    exit()
  else:
    print("\nInvalid input please choose above.")
    print("_"*45)
else:
  print("\nInvalid input.")
  print("_"*45)