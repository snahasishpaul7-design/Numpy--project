#array[start;stop;step]

#to get 2 3 4 values from the array we can use slicing method.

#For exclusion, the problem size becomes n-1 because one element is excluded.

#arr = [start:stop] , start to end-1

import numpy as np

arr = np.array([20,30,60,80,200,255,266,200,444])

print(arr[2:5]) #this will print 60,80,200

print(arr[:3]) #this will print 20,30,60 starts from index 0 to index 2

print(arr[::2]) #this will print 20,60,200,266,444 starts from index 0 to end with step size of 2f

print(arr[::-2]) #this will print 444,266,200,60,20 starts from
#index 8 to index 0 with step size of 2  

print(arr[::-1]) #this will print 444,200,266,255,200,80,60,30,20 
#starts from index 8 to index 0 with step size of 1    

