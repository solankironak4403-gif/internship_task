# 2D Array Indexing and Slicing
import numpy as np

arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])
print("second row:", arr[1])
print("element at row 2, column 3:", arr[2, 3])
print("first two rows and first three columns:\n", arr[0:2, 0:3])