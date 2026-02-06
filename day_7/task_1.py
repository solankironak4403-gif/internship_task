#Advanced Indexing and Boolean Masking
import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30])

filtered = arr[arr > 15]
print(f"Original Array: {arr}")
print(f"Filtered Array: {filtered}")
