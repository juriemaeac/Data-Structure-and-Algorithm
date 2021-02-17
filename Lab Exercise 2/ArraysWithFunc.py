'''
by Jurie Mae Castronuevo
from BSCOE 2-6
'''
def main():
    print('=' * 30)
    # Array Initialization
    array2D = []

    # Prints the array 10 numbers pero line
    printArray(array2D)

    print('-' * 30)

    # user input for row and column
    rowInput = userInput(True, 'Enter a Row: ')
    colInput = userInput(True, 'Enter a Column: ')

    print('-' * 30)

    # print entire row and column based from user input
    print(f'Row {rowInput} = {printRow(rowInput - 1, array2D)}')
    print(f'Column {colInput} = {printCol(colInput - 1, array2D)}')

    print('=' * 30)

    pass

# Print the entire array
def printArray(array):

    # print '[]' for every row to have a 2D array
    for row in range(10):
        array.append([])

        # Inserts a number whether 1 or 0 for every column in the row
        for col in range(10):

            # A condition that states whether if the column is equal to the row 
            # in order to create a diagonal structure with 1 in it and the rest 0
            if col == row:
                array[row].append(1)
            else:
                array[row].append(0)

    #print array elements
    for row in array:
        print(row)

    pass

    return array

# Print the output where spaces is used to indicate each element
def printCol(column, array):

    # print the entire column
    colPrint = array[:len(array)][column]
    output = ''

    for element in colPrint:
        output += (f'{element} ')
    
    return output

def printRow(row, array):

    # print the entire row
    rowPrint = array[row][:len(array)]
    output = ''

    for element in rowPrint:
        output += (f'{element} ')
    
    return output

# Proces user input with user handling
def userInput(error, message):

    # ser input restricted to integers 
    while error:
        num = input(message)
        try:
            num = int(num)
        except:
            print(num, 'is not an integer, Please input an integer')
        else: 
            if num > 10 or num < 1:
                print(num, 'is out of Range, Please input from 1 - 10 only')
            else:
                error = False
    
    return num

if __name__ == '__main__':
    main()
    