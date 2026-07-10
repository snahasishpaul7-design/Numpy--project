#np.concat((*array1,array2),axis=0)

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15])

arr3 = np.concatenate((arr,arr2),axis=0) #concatenates arr and arr2 along axis 0

print(arr3) #this will print [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
