'''
by Jurie Mae Castronuevo
from BSCOE 2-6
[February 17, 2021]
'''

def strcmp(str1, str2):
    if len(str1) == len(str2) and str1.lower() == str2.lower():
        return 0
    elif len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1

def main():
    print(strcmp('nasabayabasan', 'Nasabayabasan'))

    pass

if __name__ == '__main__':
    main()