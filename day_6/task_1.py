#Creating NumPy Arrays from Lists
import numpy as np

data=[1, 2, 3, 4, 5]
arr=np.array(data)
print(f"NumPy Array: {arr}")
print(f"Array Type: {(arr.dtype)}")
print(f"Array Shape: {arr.shape}")