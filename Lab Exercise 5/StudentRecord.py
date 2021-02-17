'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''

print("="*45)
print("\t\tSTUDENT RECORD")
print("="*45)
print("Enter Student record")
dict = {'ID': '', 'Name': '', 'Grades': 0, 'Remarks': ''}

dict['ID'] = input("ID: ")
dict['Name'] = input("Name: ")
q1 = int(input("Q1: "))
q2 = int(input("Q2: "))
q3 = int(input("Q3: "))
ave = int(q1+q2+q3)/3
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

