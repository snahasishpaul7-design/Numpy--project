import numpy as np

arr = np.array([1,2,3,4,np.nan,6,7,np.nan,8,9,np.nan,10])
clean = np.nan_to_num(arr) #this will replace nan with 0
print(clean) #this will print [ 1.  2.  3.  4.  0.  6.  7.  0.  8.  9.  0. 10.]






arr2 = np.array([1,2,3,4,np.nan,6,7,np.nan,8,9,np.nan,10])
clean = np.nan_to_num(arr2, nan=100) #this will replace nan with 100
print(clean) #this will print [  1.   2.   3.   4. 100.   6.   7. 100.   8.   9. 100.  10.]


