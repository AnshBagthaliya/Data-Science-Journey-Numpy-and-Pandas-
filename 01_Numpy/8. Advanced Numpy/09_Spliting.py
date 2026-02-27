"""
np.split
np.vsplit
np.hsplit
"""

import numpy as np 
arr = np.array([10,20,30,40,50,60])

# print(np.split(arr,2))
print(np.hsplit(arr,2))

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.vsplit(arr2,1))