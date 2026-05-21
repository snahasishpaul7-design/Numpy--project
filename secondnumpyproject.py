import numpy as np
data1 = []
data2 = []
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
print("Enter values for First Array")
for i in range (rows):
    row = []
    for j in range(cols):
        num = int(input("Enter the values:-"))
        row.append(num)
    data1.append(row)
print("Enter values for Second Array")
for i in range (rows):
    row = []
    for j in range(cols):
        num = int(input("Enter the values:-"))
        row.append(num)
    data2.append(row)

arr1 = np.array(data1)
arr2 = np.array(data2)

print("Your first array is:-",arr1)
print("Your second array is:-",arr2)

plus = int(input("Which operation you want to perform:-\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n  5.Modulus\n6.Exponentiation\n7.Floor Division\n Enter your choice:- "))
if plus == 1:
    print("Addition of two arrays is:-",arr1+arr2)
elif plus == 2:     
    print("Subtraction of two arrays is:-",arr1-arr2)
elif plus == 3:
    print("Multiplication of two arrays is:-",arr1*arr2)
elif plus == 4:
    print("Division of two arrays is:-",arr1/arr2)
elif plus==5:
    print("Modulus of two arrays is:-",arr1%arr2)
elif plus==6:
    print("Exponentiation of two arrays is:-",arr1**arr2)
elif plus==7:
    print("Floor Division of two arrays is:-",arr1//arr2)
else:
    print("Invalid choice")
