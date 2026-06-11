import numpy as np

data1 = []

data2 = []

rows = int(input("Enter rows:-"))
col = int(input("Enter col:-"))

for i in range(rows):
    
    row = []
    print("First value ")
    for j in range(col):
        val =  input("Enter the integer value:-")
        row.append(val)
    data1.append(row)

for i in range(rows):
    
    row1 = []
    print("Second value")
    for j in range(col):
        val1 =  input("Enter the integer value:-")
        row1.append(val1)
    data2.append(row1)

arr1 = np.array(data1)
arr2 = np.array(data2)
print(arr1)
print(arr2)

user_1 = input("Do you want to fill the array with zeros, ones, or a custom value? (yes/no):")
if user_1.lower() == "yes":
    user_2 = input("Do you want to convert the array to zero or one?:-")
    if user_2 == "zero":

        arr = np.zeros((rows, col))
        arr3 = np.zeros((rows, col))
        print(arr)
        print(arr3)

    elif user_2 == "one":

        arr = np.ones((rows, col))
        arr3 = np.ones((rows, col))
        print(arr)
        print(arr3)
        
    elif user_2 == "custom":
        
        num = input("Enter the value to fill the arrays with: ")
        
        arr = np.full((rows,col),num)
        arr3 = np.full((rows,col),num)
        print(arr)
        print(arr3)
    elif user_1.lower() == "no":
        print("Thank you")
        quit
else:
    print("Invalid....")       
        
    