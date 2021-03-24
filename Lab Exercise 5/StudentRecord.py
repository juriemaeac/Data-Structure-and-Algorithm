'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 17, 2021]
'''

print("="*45)
print("\t\tSTUDENT RECORD")
print("="*45)
print("Enter Student record")
dict = {'ID': '', 'Name': '', 'Grades': 0, 'Remarks': ''}

dict['ID'] = input("ID: ")
dict['Name'] = input("Name: ")
q1 = (input("Quiz 1: "))
q2 = (input("Quiz 2: "))
q3 = (input("Quiz 3: "))
if q1.isdigit() and q2.isdigit() and q3.isdigit():
    intq1 = int(q1)
    intq2 = int(q2)
    intq3 = int(q3)
    ave = int(intq1+intq2+intq3)/3
    dict['Grades'] = ave

    if ave >= 75:
        remarks = "Passed"
        dict['Remarks'] = remarks
    else:
        remarks = "Failed"
        dict['Remarks'] = remarks

    print("="*45)
    print("Compiling...")
    for key, value in dict.items():
        print(key, ': ', value)
    print("="*45)
else:
    print ("Please input integers only.")

