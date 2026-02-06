#Aggregation Functions with Axis
import numpy as np
arr = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
])
print(f"row-wise sum: {np.sum(arr, axis=1)}")
print(f"column-wise mean: {np.mean(arr, axis=0)}")