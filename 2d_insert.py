import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



arr2 = np.insert(arr, 1, 100, axis=0) #inserts 100 at index 1 along axis 0 (rows)

arr3 = np.insert(arr, 1, 100, axis=1) #inserts 100 at index 1 along axis 1 (columns)

arr4 = np.insert(arr, 1, [100, 200,300], axis=0) #inserts [100, 200,300] at index 1 along axis 0 (rows)

arr5 = np.insert(arr, 2, [400, 200,500], axis=1) #inserts [400, 200] at index 2 along axis 1 (columns)

print(arr2) 
print(arr3)
print(arr4)
print(arr5)


