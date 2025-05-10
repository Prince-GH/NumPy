'''
🔹 Task 1: Row-wise Addition
Create a 4x3 array of random integers between 1 and 10.
Then, create a 1D array of shape (3,) with values [10, 20, 30].
Add this 1D array to each row of the 4x3 array using broadcasting.

'''

import numpy as np

arr = np.random.randint(1, 10, (4, 3))

print(arr)


arr2 = np.array([10,20,30])

print(arr2)

print(arr+arr2)

'''
🔹 Task 2: Column-wise Addition
Create a 5x1 array with values [1, 2, 3, 4, 5].
Create a 1D array [100, 200, 300, 400] (shape 4).
Broadcast the column vector to a 5x4 result using addition.
'''

arr3 = np.array([1,2,3,4,5]).reshape(5,1)
print(arr3)
arr4 = np.array([100,200,300,400]).reshape(4)
print(arr4)
arr5 = arr3+arr4
print(arr5)
print(np.shape(arr5))

'''
🔹 Task 3: Image Normalization
Create a 3x3 image with random values from 0 to 255.
Normalize it using broadcasting to get all pixel values between 0 and 1:

normalized = (img - min) / (max - min)
Don/t use any loop.

'''

image = np.random.randint(0, 256, (3, 3))
print(image)
minpix = np.min(image)
print(minpix)
maxpix = np.max(image)
print(maxpix)
normalized = (image - minpix) / (maxpix - minpix)
print(normalized) 

'''

🔹 Task 4: Scaling Rows
Create a 4x4 array and a 1D array [1, 2, 3, 4].
Multiply the 1D array with each row of the 4x4 array (row-wise scaling).

'''

arr6 = np.random.randint(10, 50, (4, 4))
print(arr6)

arr7 = np.array([1,2,3,4]).reshape(1,4)
print(arr7)

arr8 = arr6 * arr7
print(arr8)