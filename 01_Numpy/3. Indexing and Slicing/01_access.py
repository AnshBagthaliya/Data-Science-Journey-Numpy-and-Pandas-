"""
array[inex] #1d array
array[row,column] #2d array 
"""
import numpy as np

arr  = np.array([10,20,30,40,50])

print(arr[0]) #first element
print(arr[2])
print(arr[-1])#last element

arr2 = np.array([[1,2,3],
                [4,5,6]])
print(arr2[1,0])
print(arr2[0,2])
print(arr2[1,1])

