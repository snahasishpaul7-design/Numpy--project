import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[5,6,6]])
arr3 = np.array([[[1,2,3],[5,2,6],[9,6,3],[5,6,3]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#ndim check the array dimension and for 3d you need to use [[[]]] for three times it means list of list