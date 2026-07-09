#reshape means without changing the array of data we can change the shape of the array.
#we can change the dimension of the array using reshape method without changing the data of the array.  
#reshape (column,row) specify new shape of the array.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)

reshaped_arr1 = arr.reshape(3, 3)
print(reshaped_arr)

print(reshaped_arr1) #this will give error because the total number of elements in the array is 6 and 
#we are trying to reshape it into 3x3 which requires 9 elements.   