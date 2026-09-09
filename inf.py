import numpy as np

arr = np.array([1,np.inf,3,4,5,np.inf,6,7,8,9,10])

print(np.isinf(arr)) #this will print [False  True False False False  True False False False False False]

