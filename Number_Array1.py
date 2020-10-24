str_arr = input("Enter 10 numbers:\n").split(' ') 
arr = [int(num) for num in str_arr]

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
     
    #Sorted Elements   
    print("Elements value of array in ascending order: ");    
    for i in range(0, len(arr)):    
        print(arr[i], end=" ");  
else:
    print("Invalid. Please enter 10 numbers.")
