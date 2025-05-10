# '''
# 🧠 Task 1: Temperature Conversion
# You’re given an array of temperatures in Celsius (shape 5x1). 
# Convert each to Fahrenheit using the formula:

# F = C × 9/5 + 32

# ⚙️ Steps:

# Generate random integers between 0 and 40 (Celsius).

# Use broadcasting to convert all values to Fahrenheit without any loop.
# '''

# import numpy as np

# temp = np.random.randint(0, 41, (5, 1))
# print(temp)
# temp = temp * 9/5 +32
# print(temp)

# '''
# 🧮 Task 2: Apply Image Filters (Channel-wise)
# You have a 3x3 grayscale image and a filter [0.9, 1.1, 1.0].

# Multiply each column of the image by corresponding filter value (simulate filter effect).

# '''

# Gimage = np.random.randint(0, 2,(3,3))
# print(Gimage) 
# filter = np.array([0.9, 1.1, 1.0]).reshape(3,1)
# print(filter)
# fGimage = Gimage*filter
# print(fGimage)

# '''
# 📊 Task 3: Normalize Multiple Vectors
# Generate a 4x3 matrix of random values between 0 and 100. 
# Each row is a vector. Normalize each vector row-wise using:

# normalized_row = row / row_sum

# No loops allowed.

# Ensure that shape matches original (4x3).


# '''
# print("Task 3")
# matrix = np.random.randint(0, 100, (4, 3))
# print(matrix)
# rowSum = np.sum(matrix, axis=1)
# rowSum = np.array(rowSum).reshape(len(rowSum),1)
# print(rowSum)
# normalized_row = matrix / rowSum
# print(normalized_row)


# '''
# 🧠 Expert Task: Color Channel Boosting in an Image
# You're given a 4x4x3 RGB image (3 channels: Red, Green, Blue).
# Boost each color channel by a factor:

# 🔴 Red: +20

# 🟢 Green: +10

# 🔵 Blue: +30

# '''
# print("Task 4")
# RGBImage = np.random.randint(0, 226, (4, 4, 3))
# print(RGBImage)
# factor = np.array([20, 10, 30]).reshape(3,)
# print(factor)
# filteredImg = np.clip(RGBImage + factor, 0, 255)
# print(filteredImg)


import numpy as np
import matplotlib.pyplot as plt

# Create a random RGB image (4x4 with 3 channels)
RGBImage = np.random.randint(0, 226, (4, 4, 3))

# Define the boost factors for each color channel
factor = np.array([20, 10, 30]).reshape(3,)

# Apply the boosting effect to each channel
filteredImg = np.clip(RGBImage + factor, 0, 255)

# Print the original and filtered images
print("Original Image:")
print(RGBImage)
print("\nFiltered Image:")
print(filteredImg)

#Plot both image side by side 
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

#Display the original image
axes[0].imshow(RGBImage)
axes[0].set_title("Original image")
axes[0].axis('off')

#Display the original image
axes[1].imshow(filteredImg)
axes[1].set_title("Filtered image")
axes[1].axis('off')

plt.show()


'''
🔁 Resume NumPy from "Advanced Indexing and Selection" – we finished Broadcasting.
Start from Fancy Indexing with small step-by-step tasks.
'''