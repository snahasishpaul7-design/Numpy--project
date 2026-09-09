import numpy as np

arr = np.array([1,np.inf,3,4,5,np.inf,6,7,8,9,10])

print(np.isinf(arr)) 

clean = np.nan_to_num(arr, posinf=100) #this will replace inf with 100
print(clean) #this will print [  1. 100.   3.  4.   5. 100.   6.   7.   8.   9.  10.]

