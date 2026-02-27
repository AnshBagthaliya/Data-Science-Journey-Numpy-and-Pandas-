"""
np.insert (array, index ,value,axix=None)
array - array name(Original array)
index - 
value -
axis - 
axis = 0, row-wise
1 column wise 
"""
import numpy as np 

arr = np.array([10,20,30,40,50])
print(arr)

new_arr = np.insert(arr,2,444)
print(new_arr)