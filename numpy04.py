import numpy as np

arr = np.random.randint(10, 99, (6, 6))

print(arr)

# event mask
even_mask = arr % 2 == 0
even_number = arr[even_mask]
print(even_number)

# replace all odd number with 0
arr_odd_zero  = np.where(even_mask, arr, 0)
print(arr_odd_zero)

# sum of even number
even_sum = np.sum(even_number)
print(even_sum)

#count value > 50
count_g50 = np.sum(arr>50)
print(count_g50)