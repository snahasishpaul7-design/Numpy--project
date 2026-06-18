#size is use for how many element in array or total number of element

import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(a.size)



#This is a mini project
data = []

num = int(input("Enter how many rows:-"))
num2 = int(input("Enter how many column:-"))

for i in range(num):
    
    row = []
    
    for j in range(num2):
        
        val = int(input("Enter the values:-"))
        
        row.append(val)
    data.append(row)
    
arr = np.array(data)

print(arr)

print("Your array size is",arr.size)

