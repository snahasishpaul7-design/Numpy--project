#vstack means row wise stacking
#hstack means column wise stacking

import numpy as np

arr = np.array([1,2,3])
arr1 = np.array([1,6,9])

print(np.vstack((arr)))

print(np.hstack((arr1)))