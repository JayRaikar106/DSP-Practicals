import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Reshaping
new_arr = arr.reshape(1, 9)

print("Original Array:", arr)
print("Reshaped:", new_arr)