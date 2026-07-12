import numpy as np

arr = ([[1,2,3],[4,5,6]])

new_arr = np.delete(arr,0,axis=0) #0 is the entire array

print (new_arr)