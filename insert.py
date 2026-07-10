import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr)

arr2 = np.insert(arr, 5, 100) #inserts 100 at index 5

print(arr2) #this will print [  1   2   3   4   5 100   6   7   8   9  10]