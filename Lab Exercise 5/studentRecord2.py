import math

error = True

def main():
    
    studentList = []

    while len(studentList) < 5:
        studentList.append([])

        print(f'Student {len(studentList)}')

        # Get Student Data
        identification = getID(error)
        name = getName()
        grades = getGrades(error)

        # Get average grade and remarks
        averageGrade = getAverageGrade(grades)
        remark = getRemark(averageGrade)
        
        # Input each Element to the row
        studentList[len(studentList) - 1].append(len(studentList))
        studentList[len(studentList) - 1].append(identification)
        studentList[len(studentList) - 1].append(name)
        studentList[len(studentList) - 1].append(round(averageGrade, 2))
        studentList[len(studentList) - 1].append(remark)

        print('\n')

    # Display Data
    displayData('No.', 'Student No.', 'Name', 'Grade', 'Remarks')
    for row in range(5):
        displayData(studentList[row][0], studentList[row][1], studentList[row][2], studentList[row][3], studentList[row][4])

    pass

def getName():
    name = input('Name: ')
    return name

def getID(error):
    while error:
        try:
            identification = int(input('ID: '))
        except:
            print('Invalid ID')
        else: 
            error = False

    return identification

def getGrades(error):

    gradeList = []

    while error:
        if len(gradeList) < 3:
            grades = input(f'Enter {3 - len(gradeList)} quiz<es>: ')
            gradesList = grades.split()
            for grade in gradesList:
                try:
                    intGrade = int(grade)
                except:
                    print('Invalid Input of Grade')
                else:
                    gradeList.append(intGrade)
        elif len(gradeList) > 3:
            print(f' You have entered {len(gradeList)}, remove {len(gradeList) - 3}\nYour input {gradeList}')
            toRemove = input(f'Enter {len(gradeList) - 3} number to be removed: ')
            toRemoveList = toRemove.split()
            for num in toRemoveList:
                try:
                    intNum = int(num)
                except:
                    print('Invalid Number')
                else:
                    if intNum in gradeList:
                        gradeList.pop(intNum)
        elif len(gradeList) == 3:
            error = False
    
    return gradeList

def getAverageGrade(numList):
    average = sum(numList) / len(numList)
    return average

def getRemark(num):
    remark = ''
    if 75 > num > 0:
        remark = 'Failed'
    elif 75 < num < 100:
        remark = 'Passed'

    return remark

def displayData(num, iden, name, grade, remark):
    print(f'{num:>5}{iden:>20}{name:>40}{grade:>20}{remark:>20}')

if __name__ == '__main__':
    main()