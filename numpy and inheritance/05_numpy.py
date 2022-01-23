# ndim attribute that returns an integer that tells us how many dimensions the array have

import numpy as np

arr1 = np.array(42)
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [24, 25, 26]],[[3,2,1],[8,7,6]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr2[1:4])
print(arr3.ndim)
print(arr4.ndim) 
print(arr4[0,0])
print(arr4[0,1])
print(arr4[1,0])
