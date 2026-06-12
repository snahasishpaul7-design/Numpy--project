import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape) #you can find rows and column number



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

user = input("Do you want to know how many column and row in your array:-").lower()

if user == "yes":
    
    ar1 = (arr1.shape)
    
    ar2 = (arr2.shape)
    
    print(f"In first array there are {ar1} rows and column ")
    
    print(f"In second array there are {ar2} rows and column ")
    
elif user == "no":
    exit()
    
else:
    print("Invalid expression")