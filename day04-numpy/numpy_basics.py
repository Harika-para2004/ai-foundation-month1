import numpy as np
import time

# 1. Array creation & data types
# (array, zeros, ones, arange, linspace, dtype)
arr = np.array([1, 2, 3, 4, 5])
zerosArr = np.zeros((3,4))
onesArr = np.ones((2,3))
rangeArr = np.arange(1,10,2)
linspaceArr = np.linspace(0,1,5)
print("Array:", arr)
print("Zeros Array:\n", zerosArr)
print("Ones Array:\n", onesArr)
print("Range Array:", rangeArr)
print("Linspace Array:", linspaceArr)
print("Data type of arr:", arr.dtype)
print("Data type of zerosArr:", zerosArr.dtype)
print("Data type of onesArr:", onesArr.dtype)

# 2. Shape, dimensions & reshaping
# (shape, ndim, reshape, ravel, flatten)
# ravel returns a flattened array as a view (if possible), while flatten always returns a copy.
# As a result, modifying the raveled array may affect the original array, while modifying the flattened array will not.
# So, use ravel for memory efficiency and flatten for data safety.
# Both are used to convert multi-dimensional arrays into one-dimensional arrays.
print("\n--- Shape, dimensions & reshaping ---\n")
arr2D = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", arr2D)
print("Shape of arr2D:", arr2D.shape)
print("Dimensions of arr2D:", arr2D.ndim)
reshapedArr =arr2D.reshape(3,2)
print("Reshaped Array (3x2):\n", reshapedArr)
raveledArr = arr2D.ravel()
print("Raveled Array:", raveledArr)
flattenedArr = arr2D.flatten()
print("Flattened Array:", flattenedArr)

# 3. Indexing & slicing (1D, 2D, boolean)
# (Basic indexing, fancy indexing, masks)
print("\n--- Indexing & slicing ---\n")
arr1D = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1D)
print("Element at index 2:", arr1D[2])
print("Slice from index 1 to 4:", arr1D[1:4])
arr2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:\n", arr2D)
print("Element at (1, 2)", arr2D[1,2])
print("Row 0:", arr2D[0, :])
print("Column 1:",arr2D[:, 1])
print("Elements greater than 5:", arr2D[arr2D > 5])
print("Slice of 2D array (rows 0-1, cols 1-2):\n", arr2D[0:2, 1:3])
# Fancy indexing
# Selecting specific elements using an array of indices
indices = [0, 2]
fancyIndexedArr = arr1D[indices] 
print("Fancy Indexed Array:", fancyIndexedArr) #output: [10 30]
# Boolean masking
# Creating a boolean mask to filter elements
mask = arr1D > 25
maskedArr = arr1D[mask]
print("Masked Array (elements > 25):", maskedArr) #output: [30 40 50]









