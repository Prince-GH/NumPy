import numpy as np

#creating a np array
arr = np.array([1,2,3,4,5])

print(arr)
# show the type of obj
print(type(arr))

arr2 = np.array([[5,5,16,6],[6,5,4,6]])
print(arr2)

print(arr2[0])

print(arr+1)
print(arr*2)
print(np.sum(arr2))

zero = np.zeros((2, 5))
print(zero)

one = np.ones((3,5))
print(one)

rand = np.random.randint(20, 30, (2, 4))
print(rand)


rnd = np.eye(5)
print(rnd)

# shape
img = np.array([
    [255, 0, 255],
    [0, 255, 0],
    [255, 0, 255]
])
print(img.shape) 

#reshape
arr3 = np.ones((1,6))
print(arr3)
print(arr3.reshape((2, 3)))

print("arr sum \n")
arr01 = np.random.randint(1, 10, (3,3))
print(f"arr1: \n\n{arr01}")
arr02 = np.random.randint(1, 3, (3, 3))
print(f"arr2: \n\n{arr02}")

print(f"arr1/arr2: \n\n{arr01/arr02}")