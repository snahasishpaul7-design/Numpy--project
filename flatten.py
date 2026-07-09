#in flatten there are two methods called
#.ravel() which returns a view of the original array and 
# .flatten() which returns a copy of the original array.
 
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ravel()) #this will print 1,2,3,4,5,6

print(arr.flatten()) #this will print 1,2,3,4,5,6

#difference between ravel and flatten is that ravel returns
# a view of the original array and flatten returns a copy of the original array.   