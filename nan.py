import numpy as np

arr = np.array([1,2,3,4,np.nan,6,7,np.nan,8,9,np.nan,10])

print(np.isnan(arr)) #this will print [False False False False  True False False  True False False  True False]

#true is printed where the value is nan and false is printed where the value is not nan