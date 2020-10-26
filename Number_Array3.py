#note: still not accurate, for trial only

# #numbers input split by space
num = input("Enter 10 numbers:\n").split(' ') 

#convert into integer
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

    #output
    print ("\nfirst to the highest: ", arr[9])
    print ("second to the highest: ", arr[8])
    print ("first to the lowest: ", arr[0])
    print ("second to the highest: ", arr[1])
else:
    print("Invalid. Please enter 10 numbers.")

