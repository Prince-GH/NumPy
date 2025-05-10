import numpy as np

# Create a 6x6 NumPy array with values 
# from 0 to 100 (use randint).

arr = np.random.randint(0, 100, (6, 6))

# Print the entire array.
print(f"Array: {arr}")

# frist row
print(arr[0,:])

#first column
print(arr[:,0])

#top 2x2
print(arr[0:2, 0:2])

# br 2x2
print(arr[len(arr)-2:, len(arr)-2:])

# mid row
mid = len(arr[1])/2
print(arr[3,:])

# other row
print(arr[::2,::2])

# arr[RS:RE:S, CS:CE:S]



