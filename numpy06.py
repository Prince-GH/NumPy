import numpy as np

arr = np.random.randint(0, 99, (6,6))
print(arr)

even_mask = arr%2==0
arr2 = np.where(even_mask, 1, -1)
print(arr2)

positiveOne = np.sum(arr2==1)
negativeOne = np.sum(arr2==-1)
print(f"+1s:{positiveOne} -1s:{negativeOne}")

sumRow = np.sum(arr, axis=1)
print(sumRow)
max_row_idx = np.argmax(sumRow)
print(max_row_idx)
max_row = arr[max_row_idx]
print(max_row)

arr[max_row_idx] = 999
print(arr)

