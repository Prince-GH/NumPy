import numpy as np

# Create a 3x3 array with values from 1 to 9
arr1 = np.random.randint(1, 9, (3, 3))
print(arr1)
# Create a 1D array with [100, 200, 300]
arr2 = np.array([100, 200, 300])
print(arr2)
# Add the 1D array to each row of the 3x3 array using broadcasting
print(arr1+arr2)
# Print the result
print(np.shape(arr1))
print(np.shape(arr2))

# arr3 = np.random.randint(1, 9, (2, 2))
# arr4 = np.random.randint(10, 20, (3, 3))
# print(arr3+arr4)

arr3 = np.random.randint(1, 9, (3, 3))
print(arr3)
arr4 = np.random.randint(1, 9, (3, 1))
print(arr4)
print(arr3+arr4)