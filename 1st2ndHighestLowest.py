# #numbers input split by space
num = input("Enter 10 numbers:\n").split(' ') 

#convert into integer, stored in an array
arr = [int(num) for num in num]

#used to count number of elements in an array
elements = len(arr)

if elements == 10:
    #Sort the array in ascending order 
    temp = 0; 
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp;  

    #dictionaries can't have duplicated keys
    duplicated = list(dict.fromkeys(arr))
    print (duplicated)

    #used to count number of elements in filtered list
    repeated = len(duplicated)

    if repeated == 1:
        print("\nfirst to the highest: ", duplicated[0]);   
        print("second to the highest: ", duplicated[0]); 
        print("second to the lowest: ", duplicated[0]); 
        print("first to the lowest: ", duplicated[0]); 
    else:
        #use negative indices to get the end of an array      
        print("\nfirst to the highest: ", duplicated[-1]);   
        print("second to the highest: ", duplicated[-2])
        print("second to the lowest: ", duplicated[1])
        print("first to the lowest: ", duplicated[0])
else:
    print("Please input 10 numbers!")
