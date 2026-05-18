import numpy as np

data1 = []
data2 = []

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter values for First Array")

for i in range(rows):

    row = []

    for j in range(cols):
        num = int(input("Enter value: "))
        row.append(num)

    data1.append(row)

print("Enter values for Second Array")

for i in range(rows):

    row = []

    for j in range(cols):
        num = int(input("Enter value: "))
        row.append(num)

    data2.append(row)

arr1 = np.array(data1)
arr2 = np.array(data2)
print(arr1)
print(arr2)

   