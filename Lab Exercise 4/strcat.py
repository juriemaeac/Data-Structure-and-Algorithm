'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 17, 2021]
'''

def strcat(str1, str2):
    str1 = str1 + ' ' + str2
    return str1

def main():
    new = strcat('Jurie Mae Castronuevo', 'Jurie')
    print(new)
    pass

if __name__ == '__main__':
    main()